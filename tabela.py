import pandas as pd
import numpy
import openpyxl

tab = pd.read_excel(r'C:\Users\JoaoP\Downloads\Vendas - Dez.xlsx')
print(tab)

fat = tab['Valor Final'].sum()
qtde = tab['Quantidade'].sum()
print(fat)
print(qtde)