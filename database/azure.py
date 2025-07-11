#consegui finally
#Azure
    #tentando conexão com azure
    # pesquisa referente ao azure: 
    # https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver17&tabs=windows
    # https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql
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

    conecta =  pyodbc.connect(conn_str)
    cursor = conecta.cursor()
    print('Conectado')
    
except pyodbc.Error as ex:
    print('++ex++')