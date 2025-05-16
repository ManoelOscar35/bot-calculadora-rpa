import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(20, 1057)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(20, 1057)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Escrevendo a palavra calc = calculadora no menu iniciar
posicaoMouse.typewrite('calc')

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(1)

#Movendo o mouse até a palavra calculadora
posicaoMouse.moveTo(201, 521)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(4)

#Clicando na calculadora
posicaoMouse.click(201, 521)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#print(posicaoMouse.position())