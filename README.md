
# NC Plus One API

## Setup:

From the root directory, run the following commands:

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install all dependencies:: 
   ```bash
   pip install -r requirements.txt
   ```
3. Create the databases:
   ```bash
   psql -f db/setup.sql
   ```
   To confirm both databases have been created, run:
   ```bash
   psql -l
   ```
   You should now see __nc_plus_one__ and __nc_plus_one_test__ included in the list of databases.

4. Create your .env files (these are required to connect to the database): Using the file .env.example as a template, create two files named __.env.development__ and __.env.test__ and populate these with the relevant credentials.

5. Populate the development database, nc_plus_one:
   ```bash
   python db/main.py
   ```
6. Populate the development database, nc_plus_one:
   ```bash
   ENV="test" python db/main.py
   ```





