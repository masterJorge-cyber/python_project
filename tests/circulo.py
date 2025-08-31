import pyautogui as gui
import time
import math
import numpy
# 1. Abrir o Executar (Win+R)
gui.hotkey("win", "r")
time.sleep(1)

# 2. Digitar "mspaint" e abrir
gui.typewrite("mspaint")
gui.press("enter")
time.sleep(1)  # espera o Paint abrir

# 3. Maximizar (Alt+Espaço, depois X)
# gui.hotkey("win", "up")
# time.sleep(1)
gui.moveTo(1622, 133, 1)
gui.leftClick()

# 4. Definir centro e raio do círculo (ajuste conforme sua tela)
center_x, center_y = 950, 550
raio = 150

# 5. Ir para o ponto inicial
gui.moveTo(center_x + raio, center_y)
gui.mouseDown()
angs = [210, 90, 330, 150, 270, 45,180,30,225, 315]
cords = []
# 6. Desenhar círculo
for ang in range(0, 361, 1):
    # equação parametrica do circulo

    x = center_x + int(raio * math.cos(math.radians(ang)))
    y = center_y + int(raio * math.sin(math.radians(ang)))
    if ang in angs:
        cords.append((ang, x, y))
    gui.dragTo(x, y, duration=0.1, button="left")

gui.mouseUp()

np_cords = numpy.array(cords)

print("Círculo desenhado no Paint!")

print(np_cords)

# cria um triangulo na imagem
gui.moveTo(821, 624,1)#210
gui.mouseDown(button='left')
gui.dragTo(950,400,1)
gui.dragTo(1079,624,1)
gui.dragTo(844,444,1 )
gui.dragTo(950,700,1 )
gui.dragTo(1056,444,1 )
gui.dragTo(821, 624,1)#210

gui.mouseUp()


gui.hotkey("alt", "f4")
time.sleep(1)
gui.press("right")
time.sleep(1)
gui.press("enter")
