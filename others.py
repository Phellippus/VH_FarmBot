#Para testes de código

from time import sleep
import pyautogui
from tqdm import tqdm

sleep(2)



# mouse posição atual (2 segundos após executar)
def posição_mouse():
    print(pyautogui.position())

#craftar material (2 segundos após executar)
def craft():
    while True:
        craft = pyautogui.locateOnScreen('image/forja.png', confidence=0.8)
        craft_centro = pyautogui.center(craft)
        pyautogui.moveTo(craft_centro, duration=0.5)
        pyautogui.click()
        sleep(63)

#encontrar algo na tela (2 segundos após executar)
def localizar():
    try:
        reparador = pyautogui.locateCenterOnScreen('image/reparador.png', confidence=0.8)
        if reparador:
            pyautogui.moveTo(reparador, duration=0.5)
            pyautogui.click()
            sleep(1)
    except Exception as erro:
        print('teste não encontrado')

#novo relatório temporário
def relatorio():
    teste = pyautogui.confirm(text='Código', title='Relatório', buttons=['Salvar', 'Não salvar'])

    if teste == 'Salvar':
        print('Salvo')
    else:
        print('Não salvar')
        

# funções (somente tirar o '#' para ativar)
#
# localizar()
# forjar()
# posição_mouse()
# relatorio()


# teste de tela  (somente tirar o '#' para ativar)
#
# print(pyautogui.size())
# print(pyautogui.onScreen())
# print(pyautogui.position())



#adicionar tqdm no time.sleep
#finalizar database azure do bot.py e rodar algumas vezes
#fazer usar ML pra fazer previsão do tempo total economizado e mostrar oq da pra fazer neste tempo
#fazer um relatorio com análise de dados (tratatamento de dados com pandas etc)
# projeto finalizado






# localizacao = pyautogui.locateOnScreen('chrome.png', confidence=0.8)
# print(localizacao)

# if localizacao:
#     centro = pyautogui.center(localizacao)

#     pyautogui.moveTo(centro.x, centro.y, duration=0.5)
#     sleep(0.5)
#     print(pyautogui.position())

# else:
#     print('não encontrado')




