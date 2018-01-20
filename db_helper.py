# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error

def insert_event(db_name, table, values):
    try:
        conn = sqlite3.connect(db_name)
        sql = 'insert into %s(desc, validation_votes, added_date, coin_name, proof_url, source_url, title, validation_percentage, date) values(?,?,?,?,?,?,?,?,?)' % (table)
        values = (values["desc"], values["validation_votes"], values["added_date"], values["coin_name"], values["proof_url"],values["source_url"],values["title"],values["validation_percentage"],values["date"])
        conn.execute(sql, values)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        print("inserted")
        conn.close()

def select_event(db_name, table):
    try:
        conn = sqlite3.connect(db_name)
        select_sql = 'select * from %s' %(table)
        res = conn.execute(select_sql)
        for row in res:
            print(row)
    except Error as e:
        print(e)
    finally:
        conn.close()

def is_indb(db_name, table, values):
    try:
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        coin_name = values["coin_name"]
        desc = values["desc"]
        added_date = values["added_date"]
        title = values["title"]
        date = values["date"]

        # And this is the named style:
        cur.execute("select * from coinalerts where coin_name=:coin_name and desc=:desc and added_date=:added_date and title=:title and date=:date",\
                {"coin_name": coin_name, "desc": desc, "added_date": added_date, "title": title, "date": date})
        res = cur.fetchall()
        if(len(res)):
            return True
        else:
            return False
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    values = {'desc': '"New projects to unveil, all building on ost."', 'validation_votes': '(17 votes)', 'added_date': '13 January 2018', 'coin_name': 'Simple Token (OST)', 'proof_url': 'http://coinmarketcal.com//images/proof/542992631541f7dd2d5e6d1ccba65fbf.png', 'source_url': 'https://twitter.com/betashop/status/951776366189563904', 'title': 'OST Startup Day', 'validation_percentage': '94.117647058824', 'date': '15 January 2018'}
    insert_event("./coin_alert.db", "coinalerts", values)
    select_event("./coin_alert.db", "coinalerts")
    is_indb("./coin_alert.db", "coinalerts", values)
