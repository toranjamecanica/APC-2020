from dataclasses import dataclass
import pandas as pd


dados = pd.read_csv("Despesas pelo Inep.csv")

dados_array = dados.values

mes = []
ano = []


for linha in dados_array:
    mes.append(linha[0])

print(mes.head(5))