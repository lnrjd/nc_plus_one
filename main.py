from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse

from routes.events_routes import events_router


app = FastAPI(title="NC Plus One events API")
app.include_router(events_router)


@app.exception_handler(HTTPException)
def handle_http_exception(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(RequestValidationError)
def handle_validation_error(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        message = f"Invalid {error["loc"][1]}"
    return JSONResponse(status_code=400, content={"error": {"code": "INVALID_INPUT", "message": message}})
