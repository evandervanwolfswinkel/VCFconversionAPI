import os
import urllib.parse as up
import psycopg2
import pickle
import _pickle as cPickle


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
    query = "SELECT pickledata FROM variants WHERE chromtype = 'Y';"
    cursor.execute(query)
    rows = cursor.fetchall()
    for each in rows:
        for pickledStoredList in each:
            unpickledList = cPickle.loads(pickledStoredList)
            print(unpickledList)
    conn.commit()
    cursor.close()
    conn.close()
    print("committed!")
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
        conn.close()