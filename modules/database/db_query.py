import mysql.connector
from mysql.connector import errorcode


config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'fyks',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connection was successful")


cursor = db.cursor()
cursor.execute("use users")

try:
    cursor.execute(
        "CREATE TABLE test_vs(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), age INT)")
except mysql.connector.Error as err:
    print("Table test_vs already exists")


table_name = "test_vs"


# The db.commit() method required to make the changes, otherwise no changes are made to the table.
# The cursor.fetchone() method will return the first row of the result.


def show_tables():
    print("Table list: ")
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)


def insert(table_name, name, age):
    cursor.execute("INSERT INTO {}(name, age) VALUES(\"{}\", \"{}\")".format(
        table_name, name, age))
    db.commit()


def select_all(table_name):
    print("Select all item from {}: ".format(table_name))
    cursor.execute("SELECT * FROM {}".format(table_name))
    for item in cursor:
        print(item)


def select_by_column(column_name, table_name):
    print("Select by {} column from {}: ".format(column_name, table_name))
    cursor.execute("SELECT {} FROM {}".format(column_name, table_name))
    for item in cursor:
        print(item)


show_tables()
# insert(table_name, "Vlad", 25)
select_all(table_name)
select_by_column("name", table_name)


db.close()
