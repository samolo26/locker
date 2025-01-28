import time
import os
import pyautogui
import discord_webhook 
import base64

contraseña_base64 = 'cGVwZTI2'
contraseña = base64.b64decode(contraseña_base64).decode('utf-8')

webhook = 'https://discord.com/api/webhooks/1333783677246636133/MyJ-ToLhdy-SA3_sIFaRNFJO_lkdR9uw4_5nVFC5X2Hc1kIZj66JlKiMbWzJZsJ75WoM'

def clear():
    os.system('cls')

def maximize_console():
    pyautogui.hotkey('F11')
    
def orden_ejecutora():
    os.system('shutdown -s -f -t 18')
    discord_webhook.DiscordWebhook(url=webhook, content="| INTENTO DE ACCESO |").execute()

def desorden_ejecutora():
    os.system('shutdown -a')    

def apagado_directo():
    os.system('shutdown -s -f -t 0')
    
maximize_console()
os.system('color 3')
orden_ejecutora()

title = r'''
    /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$      /$$  /$$$$$$  /$$$$$$$  /$$$$$$$ 
    | $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  /$ | $$ /$$__  $$| $$__  $$| $$__  $$
    | $$  \ $$| $$  \ $$| $$  \__/| $$  \__/| $$ /$$$| $$| $$  \ $$| $$  \ $$| $$  \ $$
    | $$$$$$$/| $$$$$$$$|  $$$$$$ |  $$$$$$ | $$/$$ $$ $$| $$  | $$| $$$$$$$/| $$  | $$
    | $$____/ | $$__  $$ \____  $$ \____  $$| $$$$_  $$$$| $$  | $$| $$__  $$| $$  | $$
    | $$      | $$  | $$ /$$  \ $$ /$$  \ $$| $$$/ \  $$$| $$  | $$| $$  \ $$| $$  | $$
    | $$      | $$  | $$|  $$$$$$/|  $$$$$$/| $$/   \  $$|  $$$$$$/| $$  | $$| $$$$$$$/
    |__/      |__/  |__/ \______/  \______/ |__/     \__/ \______/ |__/  |__/|_______/                                                                                                                                                   
'''

maximize_console()
print(title)
time.sleep(1)
clear()

print("  Que haces con mi PC malacandraculia\n")

contraseña_input = str(input("\n  Inserte la contraseña: "))

if contraseña_input == contraseña:
    discord_webhook.DiscordWebhook(url=webhook, content="| ACCESO AUTORIZADO |").execute()
    print("\n  ACCESO AUTORIZADO")
    desorden_ejecutora()
    time.sleep(1.7)
    os._exit(0)

elif contraseña_input == "9421":
    discord_webhook.DiscordWebhook(url=webhook, content="| SE HA USADO LA CONTRASEÑA DE EMERGENCIA |").execute()
    print("\n  CONTRASEÑA DE EMERGENCIA INTRODUCIDA")
    desorden_ejecutora()
    time.sleep(1.7)
    os._exit(0)

else:
    discord_webhook.DiscordWebhook(url=webhook, content="| ACCESO DENEGADO |").execute()
    time.sleep(0.8)
    for _ in range(10):
        print("\n  ACCESO DENEGADO")
    time.sleep(0.8)
    apagado_directo()

