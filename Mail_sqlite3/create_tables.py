import sqlite3

class CreateTables():
    """docstring for Creating Tables"""
    def __init__(self, cursor):
        self.cursor = cursor
        
    def create_tables(self):
        cursor.execute('''CREATE TABLE main
                    (lang_id INTEGER PRIMARY KEY int, name text)''')

    def create_tables_small(self):
        cursor.execute('''CREATE TABLE secondary
                    (lang_id INTEGER PRIMARY KEY int, table_id int, name text, email text)''')


    def insert_main(self, item):
        self.lang_id = item["id"]
        self.name = item["name"]

        query_lang = "INSERT INTO secondary VALUES(?, ?,)"
        cursor.execute(query_lang, (self.lang_id, self.name))

    def insert_secondary(self, item):
        self.lang_id = item["id"]
        self.table_id = item["table_id"]
        self.name = item["name"]
        self.email = item["email"]

        query_lang = "INSERT INTO secondary VALUES(?, ?, ?, ?)"
        cursor.execute(query_lang, (self.lang_id, self.table_id, self.name, self.email))