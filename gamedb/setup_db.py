"""run this to initialize the game database"""

import os
import sqlite3
from sqlite3 import Error


def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

fname = 'dartboardos.db'

with open('create_player.sql', 'r') as myfile:
    create_player_sql=myfile.read()
with open('create_game_header.sql', 'r') as myfile:
    create_game_header_sql=myfile.read()
with open('create_game_line.sql', 'r') as myfile:
    create_game_line_sql=myfile.read()

sql_scripts = [create_player_sql,create_game_header_sql,create_game_line_sql]

if not os.path.isfile(fname):
    conn = create_connection(fname)
    if conn is not None:
        for script in sql_scripts:
            create_table(conn,script)
    else:
        print("Error! Cannot create the database connection.")
