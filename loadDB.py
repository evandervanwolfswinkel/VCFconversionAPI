import os
import urllib.parse as up
import psycopg2
import pickle
import _pickle as cPickle

# Author: Evander van Wolfswinkel & Rick Schoenmaker
# loadDB, for loading variants from DB


def main(chromosome):
    # Main flow of the script
    conn = connection() ## Connection object
    unpickledlist = retrieveData(conn, chromosome) # Retrieve data based on chromosome filename
    return unpickledlist

def connection():
    # Set up connection with DB
    up.uses_netloc.append("postgres")
    url = up.urlparse("postgres://gjeciswx:Ax3-QX8t2FGwNnlEEXh5UaQOPTKjQEtn@dumbo.db.elephantsql.com:5432/gjeciswx")
    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port
                            )
    return conn

def retrieveData(conn, chromosome):
    # Retrieve Data from DB
    try:
        cursor = conn.cursor()
        query = "SELECT pickledata FROM variants WHERE chromtype = '{}'".format(chromosome) # SQL Query to execute finding variants
        cursor.execute(query)
        rows = cursor.fetchall() # Fetch all rows
        for each in rows:
            for pickledStoredList in each:
                unpickledList = cPickle.loads(pickledStoredList) # Unpickle bitea data from DB
        conn.commit()
        cursor.close()
        conn.close()
        return unpickledList
    except (Exception, psycopg2.DatabaseError) as error:   # If error arises, print
            print(error)
    finally:
        if conn is not None:
            conn.close()