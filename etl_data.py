#!/usr/bin/python3
import pandas as pd
import psycopg2
import time
import xlsxwriter
from yaml import safe_load


def get_config(path):
    with open(path, 'r') as stream:
        config = safe_load(stream)
    return config

def import_excel():

    oper_time = time.time()
    try:
        print ("Open excel file")
        data_frame = pd.read_excel(get_config('conf')['XLS_FNAME'], engine='openpyxl', header=3, skiprows=[4], parse_dates=True)
    except Exception as E:
        print ("ERROR:", E)
        exit(-1)
    print ("  SUCCESS at", round(time.time() - oper_time, 2), "sec")
    print ()

    oper_time = time.time()
    try:
        print ("Connect to database")
        connection = psycopg2.connect(get_config('conf')['CONN_STRING'])
    except Exception as E:
        print ("ERROR:", E)
        exit(-2)
    print ("  SUCCESS at", round(time.time() - oper_time, 2), "sec")
    print ()

    cursor = connection.cursor()
    if get_config('conf')['CTBI']:
        print ("Clear table")
        try:
            oper_time = time.time()
            cursor.execute("delete from overdue");
            connection.commit()
        except Exception as E:
            connection.rollback()
            print ("ERROR:", E)
            exit(-3)
        print ("  SUCCESS at", round(time.time() - oper_time, 2), "sec")
    else:
        print ("Clear table skipped")
    print ()

    try:
        oper_time = time.time()
        print ("Import records")
        row_id = 0;
        data=[]
        for row in data_frame.iterrows():
            isubj = str(row[1]['Субъект РФ'])
            idoz = int(row[1]['Количество\nДоз'])
            idays = int(row[1]['Просрочено дней'])
            data=(isubj,idoz,idays)                       
            cursor.execute('INSERT INTO overdue("SUBJ","DOZ","DAYS")VALUES(%s,%s,%s)',data)                      
            #connection.commit()         
            row_id += cursor.rowcount            
            #print (str(q))        
            #print (str(data))        
    except Exception as E:
        connection.rollback()
        print ("ERROR:", E)
        exit(-4)                              
    
    connection.commit()
            
    print ("  SUCCESS at", round(time.time() - oper_time, 2), "sec")
    print (str(row_id) + " records imported/updated")

    try:
        oper_time = time.time()        
        print ("Export data")              
        row_id = 0
        sq = 'select "SUBJ", sum("DOZ"), round(avg("DAYS"))from public.overdue group by 1 order by 1'
        cursor.execute(sq)
        records = cursor.fetchall()
        
        columns = ('Субъект РФ', 'Количество Доз', 'Просрочено дней')
        df = pd.DataFrame(records, columns=columns)

        writer = pd.ExcelWriter('report/report.xlsx')
        df.to_excel(writer, sheet_name='Sheet 1', index=False)
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            writer.sheets['Sheet 1'].set_column(col_idx, col_idx, column_width)
        
        writer.close()
        row_id += cursor.rowcount            

    except Exception as E:
        connection.rollback()
        print ("ERROR:", E)
        exit(-5)                              
    
    print ("  SUCCESS at", round(time.time() - oper_time, 2), "sec")
    print (str(row_id) + " records exported")

    
    return

if __name__ == '__main__':
    import_excel()
