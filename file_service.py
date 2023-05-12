import os
import json


def ler_arquivo_json():
    if os.path.isfile("config.json"):
        with open("config.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados
    else:
        return False


def criar_arquivo_json( dados):
    with open("config.json", "w") as arquivo:
        json.dump(dados, arquivo)
    return dados