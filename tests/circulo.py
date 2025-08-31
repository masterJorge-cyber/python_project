import pyautogui as gui
import time
import math
import numpy

# 1. Abrir o Executar (Win+R)
gui.hotkey("win", "r")
time.sleep(0.1)

# 2. Digitar "mspaint" e abrir
gui.typewrite("mspaint")
gui.press("enter")
time.sleep(0.5)  # tempo de espera para o Paint abrir

# 3. Maximizar (clicando no botão de maximizar)
# Essas coordenadas podem variar dependendo da resolução da sua tela.
# Ajuste conforme necessário.
gui.moveTo(1622, 133)
gui.leftClick()
time.sleep(0.1)

# 4. Definir centro e raio do círculo (ajuste conforme sua tela)
center_x, center_y = 950, 550
raio = 150

# 5. Ir para o ponto inicial
gui.moveTo(center_x + raio, center_y)
gui.mouseDown()
angs = [210, 90, 330, 150, 270, 45, 180, 30, 225, 315]
cords = []
hora_inicio = time.time()

# 6. Desenhar círculo
for ang in range(0, 361, 1):
    # equação parametrica do circulo
    x = center_x + int(raio * math.cos(math.radians(ang)))
    y = center_y + int(raio * math.sin(math.radians(ang)))
    if ang in angs:
        cords.append((ang, x, y))
    gui.dragTo(x, y, duration=0, button="left")

hora_fim =  time.time() - hora_inicio
print(f"O processo levou {hora_fim:.2f} segundos.")
gui.mouseUp()

np_cords = numpy.array(cords)

print("Círculo desenhado no Paint!")
#print(np_cords)

# cria um triangulo na imagem
gui.moveTo(821, 624)  # 210
gui.mouseDown(button='left')
gui.dragTo(950, 400)
gui.dragTo(1079, 624)
gui.dragTo(844, 444)
gui.dragTo(950, 700)
gui.dragTo(1056, 444)
gui.dragTo(821, 624)  # 210
gui.mouseUp()

# Fechar e não salvar
gui.hotkey("alt", "f4")
time.sleep(0.1)
gui.press("right")
time.sleep(0.1)
gui.press("enter")