import sqlite3
from faker import Faker
fake = Faker()


def create_person():
    con = sqlite3.connect('homework#2.db')
    cur = con.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS person(
    personid INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    Address VARCHAR(1024) NOT NULL,
    Age INTEGER NOT NULL
    )
     '''
    cur.execute(sql)
    con.close()


def insert_movies():
    for i in range(10):
        con = sqlite3.connect('homework#2.db')
        cur = con.cursor()
        sql = f'''
        INSERT INTO person (first_name, last_name, Address, Age)
        VALUES
            ("{fake.first_name()}", "{fake.last_name()}", "{fake.address()}", {fake.random_int(0,100)})
        '''
        cur.execute(sql)
        con.commit()
        con.close()


def print_person():
    con = sqlite3.connect("homework#2.db")
    cur = con.cursor()
    sql = '''
    SELECT * FROM person ORDER BY personid
    '''
    persons = cur.execute(sql)
    for item in persons:
        print(item)
    con.close()


def delete_person(personid):
    con = sqlite3.connect("homework#2.db")
    cur = con.cursor()
    sql = f'''
    DELETE FROM person WHERE personid = {personid}
    '''
    cur.execute(sql)
    con.commit()
    con.close()


def update_person(personid, age):
    con = sqlite3.connect("homework#2.db")
    cur = con.cursor()
    sql = f'''
    UPDATE person
    SET Age = {age}
    WHERE personid = {personid}
    '''
    cur.execute(sql)
    con.commit()
    con.close()


print("-" * 50)
create_person()
insert_movies()
print_person()
# print("-" * 50)
# delete_person(4)
# print_person()
# print("-" * 50)
# update_person(5, 35)
# print_person()
# print("-" * 50)
