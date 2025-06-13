import pyautogui
import time

import sqlite3 
import os 

inicio = time.time()
pyautogui.FAILSAFE = True

time.sleep(2)


# Bot não infinito -no momento- farmar cobre (5 packs media)

#
# Resolução meu PC 1366x768; 
# Serve somente para PC;
# Ative 'EASY CAMERA' nas config; - (https://snipboard.io/gC7JkR.jpg);
# Referencia easy camera, arraste o nome até o meio do minerio e deixe o EASY Camera ajustar - (https://snipboard.io/MDrkic.jpg)
# lago de la señora  - (https://snipboard.io/ZdyUfv.jpg);
# Camera afastado o mais longe possível.
#

def mouse_position(x=None, y=None):
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()
    time.sleep(70) #mude para 70sec

def ore(x=None, y=None, fase=None):
    for click1 in range(9):
        pyautogui.moveTo(x=x, y=y, duration=0.3)
        pyautogui.click()
        print(f'{fase} - Clicada número: {click1 + 1}')
        time.sleep(65)
        if click1 == 8:
            print(f'---------- {fase} Concluída! Indo para Próxima fase! ----------')      

def troca_ferramenta(x=None, y=None):
    time.sleep(1)
    pyautogui.press('i')
    time.sleep(1)
    pyautogui.moveTo(x=1203, y=211, duration=0.3)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click(button='left', clicks=2, interval=0.3)
    time.sleep(1)
    pyautogui.press('i')
    time.sleep(1)

#1ªminerio
ore(x=672, y=404, fase='1ª Fase')
troca_ferramenta(x=1157, y=304)

#2ªminerio
mouse_position(x=260, y=428)
ore(x=633, y=406, fase='2ª Fase')
troca_ferramenta(x=1196, y=307)

#3ªminerio
mouse_position(x=927, y=285)
ore(x=704, y=396, fase='3ª Fase')
troca_ferramenta(x=1239, y=308)

#4ªminerio
mouse_position(x=415, y=569)
ore(x=653, y=424, fase='4ª Fase')
troca_ferramenta(x=1283, y=306)

# 5ª minerio
mouse_position(x=1066, y=387)
ore(x=732, y=407, fase='5ª Fase')
troca_ferramenta(x=1326, y=305)

# 6ªminerio
mouse_position(x=936, y=481)
ore(x=727, y=430, fase='6ª e última fase')




def tempo():
    fim = time.time()
    tempo_total = fim - inicio

    inicio_codigo = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(inicio))
    fim_codigo = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fim))
    tempo_minutos = tempo_total / 60

    print('----------RELATORIO DO TEMPO----------')
    print(f"Início da execução: {inicio_codigo}")
    print(f"Fim da execução:    {fim_codigo}")
    print(f"Duração total:      {tempo_total:.2f} segundos ({tempo_minutos:.2f} minutos)")
    
#bank data xD
    try:
        caminho = os.path.dirname(os.path.abspath(__file__))
        db = os.path.join(caminho, 'Villagers_bot.db')
        conecta = sqlite3.connect(db)
        cursor = conecta.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS execucoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora_inicio TEXT NOT NULL,
                data_hora_fim TEXT NOT NULL,
                tempo_execucao_segundos REAL NOT NULL
            )
        ''')

        try:
            cursor.execute('ALTER TABLE execucoes ADD COLUMN mineiro TEXT')
        except sqlite3.OperationalError:
            pass  

        cursor.execute(
            "INSERT INTO execucoes (data_hora_inicio, data_hora_fim, tempo_execucao_segundos, mineiro) VALUES (?, ?, ?, ?)",
            (inicio_codigo, fim_codigo, round(tempo_total, 2), "Cobre") 
        )

        conecta.commit()
        conecta.close()
        print("Dados salvo")

    except sqlite3.Error as error:
        print(f"Erro: {error}")

tempo()
