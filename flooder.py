import pyautogui as youtube
from time import sleep
import os
os.system("color a")
# Author: Javaly
# Contato: Javaly#8240
# versao: 2.0
# Enjoy!
quest2 = float(input("digite o tempo de 1 mensagem por segundo> recomendado: 0.3: "))
quest = str(input("Digite o Texto que voce deseja floodar: "))
print ("control + C para fechar")
try:
    while True:
        youtube.write(quest)
        sleep(0.1)
        youtube.press("ENTER")
        sleep(quest2)
        print("[*] Floodando...")
        
except KeyboardInterrupt:
    print('tchau <3')