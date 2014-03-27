import sqlite3
from create_tables import CreateTables



conn = sqlite3.connect("data.db")
c = conn.cursor()

new_tables = CreateTables()
new_tables.create_tables(c)

insert = new_table.insert() 
for item in data:
    insert(item, c)

conn.commit()
conn.close()