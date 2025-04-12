#!/usr/bin/python3
import psycopg2


sql = "CREATE DATABASE etl_db WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = pg_default;"
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="127.0.0.1")
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute(sql)
    cursor.close()
    print("База данных успешно создана")
except Exception as E:
    print ("WARN:", E)
conn.close()
try:
    conn = psycopg2.connect(dbname="etl_db", user="postgres", password="postgres", host="127.0.0.1")
    cursor = conn.cursor()
    conn.autocommit = True
    f = open('etl_db.sql','r')
    txt = f.read()
    stmts = txt.split(';')
    f.close()
    for s in stmts:    
        if s is not None and s !='' :
            s+=";" 
            #print(s)
            cursor.execute(s)                

    print("Таблица создана")
except Exception as E:
    print ("WARN:", E)

cursor.close()
conn.close()