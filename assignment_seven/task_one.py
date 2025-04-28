import psycopg2
from psycopg2 import extras


def getConnection():
    connection = psycopg2.connect(dbname="postgres", user="divyanshgoenka", password="", host="localhost", port="5432")
    return connection


def table():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('''create table if not exists employees(Name Text, ID int, Age int);''')
    connection.commit()
    print("Table created\n")
    connection.close()


def insert(name, id, age):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('''insert into employees(Name, ID, Age) values (%s, %s, %s);''', (name, id, age))
    connection.commit()
    print("\nRow inserted\n")
    connection.close()


def getAll():
    connection = getConnection()
    cursor = connection.cursor(cursor_factory=extras.DictCursor)
    cursor.execute('''select * from employees;''')
    for row in cursor:
        print(dict(row))
    print("\nAll Rows fetched\n\n")
    connection.close()


table()

name = input('Enter name: ')
id = input('Enter id: ')
age = input('Enter age: ')

insert(name, id, age)

getAll()
