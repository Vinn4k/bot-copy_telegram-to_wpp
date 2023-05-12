from selenium.webdriver import Keys
from file_service import ler_arquivo_json, criar_arquivo_json
from telethon import TelegramClient, events, sync
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import pyperclip

working_dir = os.getcwd()
options = Options()

options.add_argument(f"user-data-dir={working_dir}\\User Data")
clientId=00000
clientKey="0"
messagesToWhatSapp = []

# baixa a ultima versão do chorme
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=options)

try:
    print("Inciando whatsapp")
    wait = WebDriverWait(navegador, 30)
    navegador.get("https://web.whatsapp.com/")

    grupo = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div[5]/div/div/div[1]/span')))
    print("whatsapp connectado")

    time.sleep(10)
    print("aguardando para fechar navegador")

    print("navegador principal fechado")

except:
    print("Não foi detectado login do whatsapp")

    wait = WebDriverWait(navegador, 60)
    print("indo para site de login")

    navegador.get("https://web.whatsapp.com/")
    grupo = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div[5]/div/div/div[1]/span')))
    print("whatsapp connectado")
    print("aguardando para fechar navegador")
    time.sleep(10)

    print("navegador principal fechado")

with sync.TelegramClient('projectGeremias', clientId, clientKey) as client:
    dialogs = client.get_dialogs()

    config = {}
    if ler_arquivo_json() == False:
        print("Digite o numero correspondente ao grupo")
        for i, elem in enumerate(dialogs):
            print(i, elem.title, elem.id)
        grupo = input("Digite o numero do Correspondente do grupo: ")
        print("Grupo selecionado, " + dialogs[int(grupo)].title + " " + str(dialogs[int(grupo)].id)),
        groupLink = input("Cole o link de convite do grupo do Whatsapp: ")
        print("Grupo informado: " + groupLink)

        config = criar_arquivo_json(
            {"groupNameTelegram": dialogs[int(grupo)].title, "groupIdTelegram": dialogs[int(grupo)].id,
             "groupLinkWhats": str(groupLink)})
    else:
        print("Configuração encontrada")
        config = ler_arquivo_json()

    print("Aguardando menssagens")

    navegador.get(config["groupLinkWhats"])

    @client.on(sync.events.NewMessage(chats=[config["groupIdTelegram"]], pattern='.*'))
    async def handler(event):
        print("nova mensagem")
        messagesToWhatSapp.append(event.message.message)
        #copia a menssagem
        pyperclip.copy(event.message.message)
        grupo = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
        print("Escrevendo menssagem")
        grupo.click()
        grupo.send_keys(Keys.CONTROL, 'v')
        grupo.send_keys(Keys.RETURN)

        print("Aguardando menssagens")


    client.run_until_disconnected()
