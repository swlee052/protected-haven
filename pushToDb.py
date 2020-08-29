import psycopg2
import xlrd


def pushToDb():
    '''Configuration variables'''
    user = 'postgres'
    password = '0000'
    host = 'localhost'
    port='5432'
    database='protected_haven'
    csv_path = './protected_haven.csv'
    query = """INSERT INTO orders (Daily_Date, Days, First, Second, Leader) VALUES (%s, %s, %s, %s, %s)"""


    conn = None
    try:
        conn = psycopg2.connect("host='localhost' port='5432' dbname='Ekodev' user='bn_openerp' password='fa05844d'")
        cur = conn.cursor()
        cur.execute("""truncate table "meta".temp_unicommerce_status;""")
        cur.execute("""Copy temp_unicommerce_status from 'C:\Users\n\Desktop\data.csv';""")
        conn.commit()
        conn.close()


        book = xlrd.open_workbook("protected_haven.csv")
        sheet = book.sheet_by_name("protected_haven")
        conn = psycopg2.connect (database = database, user=user, password=password, host=host, port=port)
        cur = conn.cursor()

        for r in range(1, sheet.nrows):
            Daily_Date = sheet.cell(r,0).value
            Days = sheet.cell(r,1).value
            First = sheet.cell(r,2).value
            Second = sheet.cell(r,3).value
            Leader = sheet.cell(r,4).value
            values = (Daily_Date, Days, First, Second, Leader)

            cursor.execute(query, values)



        print ""
        print ""
        columns = str(sheet.ncols)
        rows = str(sheet.nrows)
        print "I just imported Excel into postgreSQL" 

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(conn):
                cur.close()
                database.commit()
                database.close()
                conn.close()
                print("PostgreSQL connection is closed")