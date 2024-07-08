import pyautogui
import pyperclip
import webbrowser
import time
import yfinance


ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2023-01-01", end="2023-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

import pyautogui
import pyperclip
import webbrowser
import time

destinatario = "" #PARA FAZER OS TESTES BASTA INSERIR UM ENDEREÇO DE E-MAIL VÁLIDO EX: teste123@gmail.com
assunto = "Análises do projeto 2023"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

atte.
"""

# Abrir o navegador e ir para o gemail 
webbrowser.open("www.gmail.com")
time.sleep(3)

#Configurando uma pausa de 3 segundos.
pyautogui.PAUSE = 5

# Clicar no botão escrever 
pyautogui.click(x=84, y=216)

# Digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão enviar
pyautogui.click(x=844, y=683)

# Fechar gmail
pyautogui.hotkey("ctrl", "f4")

print("Email enviado com sucesso!")