import psycopg2
import csv

def pullFromDb():
    '''Configuration variables'''
    user = 'postgres'
    password = '0000'
    host = 'localhost'
    port='5432'
    database='protected_haven'
    

    conn = None

    try:
        conn = psycopg2.connect(user = user,
                                password = password,
                                host = host,
                                port = port,
                                database = database)
        cur = conn.cursor()
        
        cur.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
        for table in cur.fetchall():
            table = str(table) #parse string
            table = table[2:-3]

            '''Configuration variables'''
            query = f'SELECT * FROM {table}'
            csv_path = f'protected_haven_{table}.csv'

            cur.execute(query)
            num_fields = len(cur.description)
            field_names = [i[0] for i in cur.description]
            rows = cur.fetchall()
            fp = open(csv_path, mode='w')
            myFile = csv.writer(fp)
            myFile.writerows(rows)
            fp.close()
            print (f"{csv_path} file generation successful")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(conn):
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

pullFromDb()
    



