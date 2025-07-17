import sqlite3


def save_sqlite(
    data_execucao, data_fim, duracao_minutos, qtd_reparadores, ferramentas_concertadas,relatorio_guardar):
    conn = sqlite3.connect('dados_bot.db')
    cursor = conn.cursor()

# cria tabela principal 
    cursor.execute('''    
        CREATE TABLE if NOT EXISTS  execucao_do_bot(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_execucao DATETIME NOT NULL,
            data_fim DATETIME NOT NULL,
            duracao_minutos FLOAT,
            qtd_reparadores INTEGER DEFAULT 0,
            ferramentas_concertadas INTEGER DEFAULT 0,
            relatorio_guardar BOOLEAN DEFAULT 0
        ) '''
    )

# add dados sempre que executado e evitar sqli
    cursor.execute('''
        INSERT INTO execucao_do_bot (
            data_execucao, data_fim, duracao_minutos,
            qtd_reparadores, ferramentas_concertadas, relatorio_guardar
        ) VALUES (?, ?, ?, ?, ?, ?)   
    ''', (
        data_execucao, data_fim, duracao_minutos,
        qtd_reparadores, ferramentas_concertadas, relatorio_guardar
    ))

# salva e fecha
    conn.commit()
    conn.close()