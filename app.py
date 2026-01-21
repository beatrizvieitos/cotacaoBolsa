import pandas as pd
import yfinance as yf

opcao = "" #Variável de controle

while True:
    acao = input("Insira o nome da ação em bolsa que deseja consultar: ")
    inicio = input("Insira a data de início da cotação: ")
    fim = input("Insira a data de fim da cotação: ")

    #Obter os dados de cotação em bolsa
    df= yf.download(acao, start=inicio, end=fim)

    print(df)

    opcao = input("Deseja consultar outra ação? (Sim/Não): ").lower()

    if opcao == "não":
        print("Operação finalizada.")
        break

