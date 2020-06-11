import os
import urllib.parse as up
import psycopg2
import pickle

# Author: Evander van Wolfswinkel & Rick Schoenmaker
# connectDB, Connect with Database and insert chromosome as bitea binary strings

with open("./static/1", "rb") as f:
    unpickle = pickle.load(f) # Load pickled variants dictionary

# Load in as pickles python variable in memory
picklefile = pickle.dumps(unpickle)

# Connect with database
up.uses_netloc.append("postgres")
url = up.urlparse("postgres://gjeciswx:Ax3-QX8t2FGwNnlEEXh5UaQOPTKjQEtn@dumbo.db.elephantsql.com:5432/gjeciswx")
conn = psycopg2.connect(database=url.path[1:],
                        user=url.username,
                        password=url.password,
                        host=url.hostname,
                        port=url.port
                        )

try:
    cursor = conn.cursor()
    query = "INSERT INTO variants(ChromType, PickleData) VALUES (%s, %s)"  # query for inserting chromosome and pickled bitea data
    cursor.execute(query, ("1",psycopg2.Binary(picklefile),))  # Insert data into %s
    conn.commit()
    cursor.close()
    conn.close()
    print("committed!")
except (Exception, psycopg2.DatabaseError) as error:  # If error arises; print
        print(error)
finally:
    if conn is not None:
        conn.close()