#!/usr/bin/env python
import pandas as pd
import sqlite3

with sqlite3.connect("../DATA/presidents.db") as s3conn:  # <1>

    s3cursor = s3conn.cursor()  # <2>

    # select first name, last name from all presidents
    s3cursor.execute('''
        select firstname, LASTNAME
        from presidents
        where firstname = 'John'
    ''')  # <3>

    print("Sqlite3 does not provide a row count\n")  # <4>

    for row in s3cursor.fetchall():  # <5>
        print(row)  # <6>


    df = pd.read_sql_query("select * from presidents", s3conn)
    print(df.head())

    print(df.deathdate)
