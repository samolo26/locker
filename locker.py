import time
import os
import base64
import ctypes
import threading

contraseña_base64 = 'cGVwZTI2'
contraseña = base64.b64decode(contraseña_base64).decode('utf-8')

webhook = 'https://discord.com/api/webhooks/1333783677246636133/MyJ-ToLhdy-SA3_sIFaRNFJO_lkdR9uw4_5nVFC5X2Hc1kIZj66JlKiMbWzJZsJ75WoM'

def clear():
    os.system('cls')

def maximize_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 3)  # Maximiza la ventana

def orden_ejecutora():
    os.system('shutdown -s -f -t 18')
    def send_webhook():
        import discord_webhook
        discord_webhook.DiscordWebhook(url=webhook, content="| INTENTO DE ACCESO |").execute()
    threading.Thread(target=send_webhook, daemon=True).start()

def desorden_ejecutora():
    os.system('shutdown -a')    

def apagado_directo():
    os.system('shutdown -s -f -t 0')

os.system('color 3')

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
print(title)    
orden_ejecutora()
maximize_console()
clear()

print("  Que haces con mi PC malacandraculia\n")

contraseña_input = str(input("\n  Inserte la contraseña: "))

def send_webhook(content):
    import discord_webhook
    discord_webhook.DiscordWebhook(url=webhook, content=content).execute()

if contraseña_input == contraseña:
    threading.Thread(target=send_webhook, args=("| ACCESO AUTORIZADO |",), daemon=True).start()
    print("\n  ACCESO AUTORIZADO")
    desorden_ejecutora()
    time.sleep(1.7)
    os._exit(0)

elif contraseña_input == "9421":
    threading.Thread(target=send_webhook, args=("| SE HA USADO LA CONTRASEÑA DE EMERGENCIA |",), daemon=True).start()
    print("\n  CONTRASEÑA DE EMERGENCIA INTRODUCIDA")
    desorden_ejecutora()
    time.sleep(1.7)
    os._exit(0)

else:
    threading.Thread(target=send_webhook, args=("| ACCESO DENEGADO |",), daemon=True).start()
    time.sleep(0.8)
    for _ in range(10):
        print("\n  ACCESO DENEGADO")
    time.sleep(0.8)
    apagado_directo()

