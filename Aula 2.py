#Passo 1: import the sales base

import pandas as pd

tabela = pd.read_csv('telecom_users.csv')

#Passo 2: changing to better

#coluna inútil(unnamed)
#axis = 0 --> linha
#axis = 1 --> coluna

tabela = tabela.drop('Unnamed: 0', axis=1)
print(tabela)

#Date processing
#transformando elementos no type errado (total gasto = object --> float)
#Se a transformação de nome a número der erro --> valor vazio = 'coerce'

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
print(tabela.info())

#valores vazios(Nan)

#colunas vazias
#excluir colunas vazias
#how= 'all'> coluna completamente vazia
#how= 'any'-> coluna que tem pelo menos 1 valor vazio

tabela = tabela.dropna(how='all', axis=1)

#excluir linhas vazias

tabela = tabela.dropna(how='any', axis=0)

#Passo 3: Initial review

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Passo 4: Detailed analisys

import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
