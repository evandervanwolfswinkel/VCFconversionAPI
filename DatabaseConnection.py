import psycopg2
import urllib.parse as up
import pickle


up.uses_netloc.append("postgres")
url = up.urlparse("postgres://gjeciswx:Ax3-QX8t2FGwNnlEEXh5UaQOPTKjQEtn@dumbo.db.elephantsql.com:5432/gjeciswx")
try:
    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)

    cursor = conn.cursor()
    #
    # query = "INSERT INTO variants(chromtype, pickledata) VALUES (%s, %s)"
    # with open("./static/Y", "rb") as f:
    #     unpickle = pickle.load(f)
    #
    # picklefile = pickle.dumps(unpickle)
    # cursor.execute(query, ("Y", psycopg2.Binary(picklefile),))
    print(cursor.execute("SELECT pickledata from variants WHERE chromtype ='X';"))
    conn.commit()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if (conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")


