#!/usr/bin/python3
import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="127.0.0.1")

cursor = conn.cursor()
conn.autocommit = True

sql = "drop database etl_db;"

cursor.execute(sql)

cursor.close()
conn.close()