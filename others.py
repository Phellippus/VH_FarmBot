#Para testes

import time
import pyautogui
from tqdm import tqdm

time.sleep(2)

# mouse posição atual (2 segundos após executar)
def posição_mouse():
    print(pyautogui.position())

#forjar material (2 segundos após executar)
def forjar():
    while True:
        pyautogui.moveTo(x=834, y=552)
        pyautogui.click()
        time.sleep(63)

#encontrar algo na tela (2 segundos após executar)
def localizar():
    try:
        reparador = pyautogui.locateCenterOnScreen('image/reparador.png', confidence=0.8)
        if reparador:
            pyautogui.moveTo(reparador, duration=0.5)
            pyautogui.click()
            time.sleep(1)
    except Exception as erro:
        print('teste não encontrado')


#ativar funções (somente tirar o '#' para ativar)
# localizar()
#forjar()
#posição_mouse()




#adicionar tqdm no time.sleep
#finalizar database azure do bot.py e rodar algumas vezes
#fazer usar ML pra fazer previsão do tempo total economizado e mostrar oq da pra fazer neste tempo
#fazer um relatorio com análise de dados (tratatamento de dados com pandas etc)
# projeto finalizado