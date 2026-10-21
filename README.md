
# Instructions: How to use nc_plus_one

## Initial set up:

* Create and open a virtual environment
* Install all dependencies from the requirements file, byt running the following on the command line: pip install -r requirements.txt


Now, we can start with a clean database setup:

## Datbase setup:

Create a new database, nc_plus_one, as follows:
1. Open the file db/seed.sql
2. Check the database name is correct
3. Run the following from the command line: psql -f setup.sql
4. To confirm the database now exists, run the following from the command line: psql -l

You should now see __nc_plus_one__ included in the list of databases.


## Create .env file:

This is required to connect to the database.

Using the file .env.example as a template, create a file named __.env.development__ and populate this with the relevant credentials.