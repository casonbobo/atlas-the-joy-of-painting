
# import pandas as pandas
import csv
import psycopg2
from psycopg2 import sql

#/var/lib/postgresql/14/main

    # CONNECT TO DATBASE
conn = psycopg2.connect(
    dbname="DATABASE_joc",
    user="postgres",
    password="password",
    host="127.0.0.1",
    port="5432"
)
# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Name of the table to insert data into
table_name = "episodeSubjects"
# Open the CSV file
with open("clean_data/episodeSubjects.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        columns = ", ".join(row)
        values = ", ".join(["%s"] * len(row))
        insert_query = f"INSERT INTO episodeSubjects VALUES ({values})"

        # Execute the INSERT statement
        cur.execute(insert_query, row)

conn.commit()
cur.close()
conn.close()
