from fastapi import FastAPI

from routes.events_routes import events_router


app = FastAPI(title="NC Plus One events API")
app.include_router(events_router)

