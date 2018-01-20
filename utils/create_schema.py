# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error
from . import extract_events

def create_schema(db_name):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        create_table = '''create table coinalerts (id INTEGER PRIMARY KEY AUTOINCREMENT, title text,
                  source_url text, date text, validation_percentage int, desc text, proof_url text, validation_votes text, coin_name text, added_date text)'''
        c.execute(create_table)
        conn.commit()
        print( "success !!")
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_schema("./coin_alert.db")
