import os
import urllib.parse as up
import psycopg2
import pickle


with open("./static/Y", "rb") as f:
    unpickle = pickle.load(f)

picklefile = pickle.dumps(unpickle)

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
    query = "INSERT INTO variants(ChromType, PickleData) VALUES (%s, %s)"
    cursor.execute(query, ("Y",psycopg2.Binary(picklefile),))
    conn.commit()
    cursor.close()
    conn.close()
    print("committed!")
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
        conn.close()