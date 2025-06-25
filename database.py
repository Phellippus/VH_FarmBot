
import pyodbc

driver = '{ODBC Driver 17 for SQL Server}'
server = 'botvillagersdatabase.database.windows.net'
database = 'results_bot.db'
    
conn_str = (
    f"DRIVER={driver};"
    f"SERVER=tcp:{server};" 
    f"DATABASE={database};"
    f"Authentication=ActiveDirectoryInteractive;"
)
    
try:
    with pyodbc.connect(conn_str):
        print("[teste")
            
except pyodbc.Error as ex:
    print('++ex++')