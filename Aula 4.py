import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tab = pd.read_csv('advertising.csv')
print(tab)

#date processing
print(tab.info())

#criar gráfico: sns...
sns.heatmap(tab.corr(), cmap ='Wistia', annot=True) #correlação entre os dados

#exibir gráfico: plt.show()
plt.show()

#Passo 2: building a I.A
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

#Criando a I.A
regressaolinear = LinearRegression()
arvoredecisao = RandomForestRegressor()

#Treinando a I.A
regressaolinear.fit(x_treino, y_treino)
arvoredecisao.fit(x_treino, y_treino)

#Qual modelo é melhor
#Testes
#O maior R² é o melhor modelo
regressaolinear = regressaolinear.predict(x_teste)
arvoredecisao = arvoredecisao.predict(x_teste)

prev1 = metrics.r2_score(y_teste, regressaolinear)
prev2 = metrics.r2_score(y_teste, arvoredecisao)

print('{:.1%}'.format(prev1))
print('{:.1%}'.format(prev2))

tab_auxiliar = pd.DataFrame()
tab_auxiliar['y_teste'] = y_teste
tab_auxiliar['Previsao Regressao Linear'] = regressaolinear
tab_auxiliar['Previsao Arvore Decisao'] = arvoredecisao

plt.figure(figsize=(10,6))
sns.lineplot(data=tab_auxiliar)
plt.show()

#How to do a new prevision?
#Importar uma nova tabela com as informações de TV, Rádio e Jornal
#passa a nova tabela para o predict do seu modelo

novos = pd.read_csv('novos.csv')
print(novos)

previsao = arvoredecisao.predict(novos)
print(previsao)