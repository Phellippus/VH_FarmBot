# Bot não infinito para farmar (5/7 packs media)

#
# 6 ferramentas recomendado
# Resolução recomendada 1366x768; 
# Serve somente para PC;
# Ative 'EASY CAMERA' nas config; - (https://snipboard.io/gC7JkR.jpg);
# Camera afastado o mais longe possível.
#                     Código e bot em construção...
#
from database.data import save_sqlite
from tqdm import tqdm
import pyautogui
import time


pyautogui.FAILSAFE = True #Serve para parar código, coloque o mouse no canto superior esquerdo (x=0,y=0)
time.sleep(2)

#contadores
qtd_reparador = 0
sleep_tqdm = 65 # tempo para rodar
controlador_sleep = 1 # controlar por quanto tempo cada barra do tqdm vai demorar

#adicionar tqdm no time.sleep
def sleep_com_barra():
    for i in tqdm(range(sleep_tqdm), desc='Restante...', dynamic_ncols=True):
        time.sleep(controlador_sleep)

# funções 
def mouse_position(x=None, y=None):
    pyautogui.moveTo(x=x, y=y, duration=0.3)
    pyautogui.click()
    time.sleep(70)

def item(x=None, y=None, fase=None):
    global qtd_reparador #modificar 0 dos contadores

    for click1 in range(9):
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

        sleep_com_barra() #tqdm de 65 segundos com sleep
        
        if click1 == 8:
            print(f'{fase} - Clicada número: {click1}')
            print(f'---------- {fase} Concluída! Indo para Próxima fase! ----------')      

def troca_ferramenta(x=None, y=None):
    def pausa(): time.sleep(1)
    pausa()
    pyautogui.press('i') #botão do inventario
    pausa()
    pyautogui.moveTo(x=1203, y=211, duration=0.3) #botão do 3ª slot
    pyautogui.click()
    pausa()
    pyautogui.moveTo(x=x, y=y, duration=0.3) #serve para próxima ferramenta
    pyautogui.click(button='left', clicks=2, interval=0.3)
    pausa()
    pyautogui.press('i') #fecha inventario
    pausa()


# temporizador + database
def tempo():
    fim = time.time()
    tempo_total = fim - inicio

    inicio_codigo = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(inicio))
    fim_codigo = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(fim))

    tempo_minutos = tempo_total / 60
    pickaxe_concertado = qtd_reparador // 10
    
    #irá aparecer um aviso do relatório com as opções salvar e não salvar (others.py tem exemplo em def relatorio)
    relatorio = pyautogui.confirm(text=f'''
                            RELATORIO\n
                            Início da execução: {inicio_codigo}
                            Fim da execução:    {fim_codigo}
                            Duração total:      {tempo_total:.2f} segundos ({tempo_minutos:.2f} minutos)
                            {'-' * 65}
                            {qtd_reparador} reparadores encontrados
                            {pickaxe_concertado} picaretas concertadas
                    '''
                            ,title='CÓDIGO FINALIZADO', buttons=['Salvar', 'Não salvar']
                )

    # futuramente caso desejar salvar .xlsx ou em .csv ou outras possibilidades.
    if relatorio == 'Salvar':
        pass    
    else:
        print('Não salvar')
    
   
    if relatorio == 'Salvar':
        save_sqlite(
            data_execucao=inicio_codigo,
            data_fim=fim_codigo,
            duracao_minutos=round(tempo_minutos, 2),
            qtd_reparadores=qtd_reparador,
            ferramentas_concertadas=pickaxe_concertado,
            relatorio_guardar=True
        )
    else:
        save_sqlite(
            data_execucao=inicio_codigo,
            data_fim=fim_codigo,
            duracao_minutos=round(tempo_minutos, 2),
            qtd_reparadores=qtd_reparador,
            ferramentas_concertadas=pickaxe_concertado,
            relatorio_guardar=False
        )
    #
    #Azure
    #tentando conexão com azure
   
 
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
    time.sleep(2)
    print(pyautogui.position())

    tempo() 

