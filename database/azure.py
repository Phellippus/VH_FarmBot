import os
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

try:
     conn = get_conn()
     cursor = conn.cursor()

     cursor.execute(""""
                CREATE TABLE execucao_bot (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_execution DATETIME NOT NULL,
            data_end DATETIME NOT NULL,
            minutes_duration FLOAT,
            qtd_reparadores INTEGER DEFAULT 0
            tool_fixed INTEGER DEFAUL 0,
            report_data BOOLEAN DEFAULT 0
                    
                    
                    );
                """
     )
    
except Exception as error:
    print('Table already exist')



#Desenvolvimento e Desafios Técnicos
#
# Durante o desenvolvimento do projeto, enfrentei diversos desafios que contribuíram significativamente para meu aprendizado. 
# (como pode ser observado desde os primeiros commits no repositório).
# Embora o código do bot em si seja relativamente simples e cubra funcionalidades básicas, 
# o maior obstáculo esteve relacionado ao banco de dados.
#
# Inicialmente, meu conhecimento em SQL estava focado em operações fundamentais, 
# como criação de tabelas e tratamento de erros simples. 
# No entanto, ao tentar construir algo mais próximo de um ambiente profissional, 
# percebi que a complexidade vai muito além da sintaxe: 
# é necessário considerar segurança, tratamento de exceções, organização eficiente dos dados e boas práticas de arquitetura de banco de dados — 
# temas pouco abordados em materiais introdutórios.
#
# O código atual representa o que consegui implementar com o conhecimento que tenho até o momento, 
# mas sigo em constante aprendizado e aprimoramento, 
# sempre buscando evoluir tanto tecnicamente quanto na qualidade das soluções desenvolvidas.
#


