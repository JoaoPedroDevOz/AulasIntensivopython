from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

nav = webdriver.Chrome()

#Passo 1: Get the dollar, euro and gold quote
nav.get('https://www.google.com.br/')

#Pegando a cotação do dolar
nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação dolar') #pesquisa na barra de navegação
nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) #Enter
dolar = nav.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') #Pegar o valor

print(f'R$ {dolar:.4}')

#Pegando a cotação do euro
nav.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').click()
nav.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').clear()
nav.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').send_keys('Cotação euro')
nav.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro = nav.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(f'R$ {euro:.4}')

#Pegando a cotação do ouro
nav.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').click()
nav.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').clear()
nav.get('https://www.melhorcambio.com/ouro-hoje')
ouro = nav.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
ouro = ouro.replace(',', '.')
print(f'R$ {ouro}')

#Fechando o navegador
nav.quit()

#Passo 3: Import the base and update the quotes in my base
import pandas as pd

tab = pd.read_excel('Produtos.xlsx')


#Passo 4: Calculate the new prices and save/ export to the sales base
#loc[linhas, coluna]

tab.loc[tab['Moeda'] == 'Dólar', 'Cotação'] = float(dolar)
tab.loc[tab['Moeda'] == 'Euro', 'Cotação'] = float(euro)
tab.loc[tab['Moeda'] == 'Ouro', 'Cotação'] = float(ouro)

#atualizando pre;os
#preço de compra = cotaçao * preço original
#preço de venda = preço de compra * margem
tab['Preço de Compra'] = tab['Preço Original'] * tab['Cotação']
tab['Preço de Venda'] = tab['Preço de Compra'] * tab['Margem']
print(tab)

#Passo 5: Exporting like a new document
tab.to_excel('Produtos Novos.xlsx', index=False)
