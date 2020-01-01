import psycopg2

config = {
    'database': 'btredb',
    'user': 'vladyslavlietun',
    'password': 'root',
    'host': 'localhost',
    'port': 5432
}

# def connect():
""" Connect to the PostgreSQL database server """
db = None
try:
    db = psycopg2.connect(**config)
    print("Connect successful!!!")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if db is not None:
        db.close()
        print('Database connection closed.')
