import mysql.connector

class EZ_Query:
    def __init__(this, __SQL_H=None, __SQL_UN=None, __SQL_PW=None, __SQL_DB=None):
        this.host = __SQL_H
        this.user = __SQL_UN
        this.passwd = __SQL_PW
        this.db = __SQL_DB

        this.mydb = mysql.connector.connect(
            host = this.host,
            user = this.user,
            passwd = this.passwd,
            db = this.db
        )

    def create_database(this, __DBNAME):
        dbc = this.mydb.cursor()
        dbc.execute('create database ' + __DBNAME)
        print('Database Created')

    def create_table(this, __TBNAME, __CONTENT):
        dbc = this.mydb.cursor()
        query = 'create table {}(id int auto_increment primary key not null, {})'.format(__TBNAME, __CONTENT).replace('::', ' text')
        dbc.execute(query)
        print('Table Created')

    def insert_into(this, __TBNAME, __CONTENTS):
        dbc = this.mydb.cursor()
        keys = ', '.join(__CONTENTS.keys())
        values = "'"+"', '".join(__CONTENTS.values())+"'"
        query = 'insert into {}({}) values({})'.format(__TBNAME, keys, values)
        dbc.execute(query)
        this.mydb.commit()
        print(dbc.rowcount, "record inserted, ID: ", dbc.lastrowid)

    def select(this, __TBNAME):
        dbc = this.mydb.cursor()
        dbc.execute('select * from ' + __TBNAME)
        for x in dbc.fetchall():
            print(x)

    def update(this, __TBNAME, __COL, __COL_VAL, __ID):
        dbc = this.mydb.cursor()
        query = "update {} set {}='{}' where id={}".format(__TBNAME, __COL, __COL_VAL, __ID)
        dbc.execute(query)
        this.mydb.commit()
        print('Record ID '+str(__ID)+' updated')

    def delete(this, __TBNAME, __ID):
        dbc = this.mydb.cursor()
        query = "delete from {} where id='{}'".format(__TBNAME, __ID)
        dbc.execute(query)
        this.mydb.commit()
        print('Deleted record ID '+__ID)

    def truncate(this, __TBNAME):
        dbc = this.mydb.cursor()
        dbc.execute('truncate ' + __TBNAME)
        print('All table records deleted')

    def drop_table(this, __TBNAME):
        dbc = this.mydb.cursor()
        query = 'drop table {}'.format(__TBNAME)
        dbc.execute(query)
        print('Table Deleted')

    def drop_database(this, __DBNAME):
        dbc = this.mydb.cursor()
        dbc.execute('drop database ' + __DBNAME)
        print('Database Deleted')
