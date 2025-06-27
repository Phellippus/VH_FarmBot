# Bot não infinito para farmar (5/7 packs media)

#
# 6 ferramentas recomendado
# Resolução recomendada 1366x768; 
# Serve somente para PC;
# Ative 'EASY CAMERA' nas config; - (https://snipboard.io/gC7JkR.jpg);
# Camera afastado o mais longe possível.
#                     Código e bot em construção...
#

from tqdm import tqdm
import pyautogui
import time
import pyodbc


pyautogui.FAILSAFE = True #Serve para parar código, coloque o mouse no canto superior esquerdo (x=0,y=0)
time.sleep(2)

#contadores
qtd_reparador = 0


# funções 
def mouse_position(x=None, y=None):
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()
    time.sleep(70)

def item(x=None, y=None, fase=None):
    global qtd_reparador #modificar 0 dos contadores

    for click1 in tqdm(range(9),desc=fase, ncols=70):
        try:
            reparador = pyautogui.locateCenterOnScreen('image/reparador.png', confidence=0.8)
            if reparador:
                pyautogui.moveTo(reparador, duration=0.5)
                pyautogui.click()
                qtd_reparador += 1
                time.sleep(1)
        except Exception as erro:
            print('Reparador não encontrado')
        pyautogui.moveTo(x=x, y=y, duration=0.3)
        pyautogui.click()
        print(f'{fase} - Clicada número: {click1 + 1}')
        time.sleep(65)
        if click1 == 8:
            print(f'{fase} - Clicada número: {click1}')
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



# temporizador + azure
def tempo():
    fim = time.time()
    tempo_total = fim - inicio

    inicio_codigo = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(inicio))
    fim_codigo = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fim))

    tempo_minutos = tempo_total / 60
    pickaxe_concertado = qtd_reparador // 10

    print('----------RELATORIO----------')
    
    print(f" Início da execução: {inicio_codigo}")
    print(f"Fim da execução:    {fim_codigo}")
    print(f"Duração total:      {tempo_total:.2f} segundos ({tempo_minutos:.2f} minutos)")
    print('-' * 15)
    print(f'{qtd_reparador} reparadores encontrados')
    print(f'{pickaxe_concertado} picaretas concertadas')
        
    
    #
    #Azure
    #tentando conexão com azure
    # pesquisa referente ao azure: 
    # https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver17&tabs=windows
    # https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql
    
   
# driver = '{ODBC Driver 17 for SQL Server}'
# server = 'botvillagersdatabase.database.windows.net'
# database = 'results_bot.db'
 
#execução principal
if __name__ == "__main__":

    inicio = time.time()

    #1ªminerio
    item(x=672, y=404, fase='1ª Fase')
    troca_ferramenta(x=1157, y=304)

    #2ªminerio
    mouse_position(x=260, y=428)
    item(x=633, y=406, fase='2ª Fase')
    troca_ferramenta(x=1196, y=307)

    #3ªminerio
    mouse_position(x=927, y=285)
    item(x=704, y=396, fase='3ª Fase')
    troca_ferramenta(x=1239, y=308)

    #4ªminerio
    mouse_position(x=415, y=569)
    item(x=653, y=424, fase='4ª Fase')
    troca_ferramenta(x=1283, y=306)

    #5ª minerio
    mouse_position(x=1066, y=387)
    item(x=732, y=407, fase='5ª Fase')
    troca_ferramenta(x=1326, y=305)

    #6ª minerio
    mouse_position(x=936, y=481)
    item(x=727, y=430, fase='6ª e última fase')
    print(pyautogui.position())

    tempo() 