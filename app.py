import pyautogui
from time import sleep

# 1 - clicar e digitar meu usuario
pyautogui.click(709,388, duration=2)
pyautogui.write('allan')

# 2 - clicar e digitar minha senha
pyautogui.click(710,409, duration=2)
pyautogui.write('150322')

# 3 - clicar em "Entrar"
pyautogui.click(609,439, duration=2) 

# 4 - extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]   
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]   
        
        # 1 - clicar e digitar produto
        pyautogui.click(426,375, duration=2)
        pyautogui.write(produto)    

        # 2 - clicar e digitar quantidade
        pyautogui.click(440,405, duration=2)
        pyautogui.write(quantidade)

        # 3 - clicar e digitar preço
        pyautogui.click(443,434, duration=2)
        pyautogui.write(preco)

        # 4 - clicar em "Registar"
        pyautogui.click(324,586, duration=2)
        sleep(1)


 