#passo 1: Enter in system
import time
import pyautogui
import pyperclip

pyautogui.PAUSE = 2

#passo 1: Browse the system(even the exportation)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh')
pyautogui.press('enter')
time.sleep(15)

#passo 2: Download the sales base
pyautogui.click(x=425, y=250, button='left')
pyautogui.click(x=1735, y=146)
pyautogui.click(x=1519, y=536)
time.sleep(15)

#passo 3: Import sales base for python
import pandas as pd
import numpy
import openpyxl

tab = pd.read_excel(r'C:\Users\JoaoP\Downloads\Vendas - Dez.xlsx')
print(tab)

#passo 4: Calculate billing and quantity of products sold
fat = tab['Valor Final'].sum()
qtde = tab['Quantidade'].sum()
print(fat)
print(qtde)

#passo 5: Forward(send) the e-mail to directory
pyautogui.hotkey('ctrl', 't')
time.sleep(5)
pyautogui.click(x=1717, y=130)
time.sleep(15)
pyautogui.click(x=70, y=170)
time.sleep(5)
pyperclip.copy('joaopedromaximovhth@gmail.com')

pyautogui.hotkey('ctrl', 'v')
pyperclip.copy('Relatório de Vendas')
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = '''
Dear

The yesterday billing was by R$ {:,.2f} 

And the quantity of products sold was {:,}

Abs
Joao Pedro
'''.format(fat, qtde)

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')