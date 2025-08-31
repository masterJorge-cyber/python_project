import pyautogui as gui
import time

print("O script vai começar em 3s...")
time.sleep(3)

print("Movendo o mouse... mexa manualmente para encerrar.")

# posição inicial
last_pos = gui.position()

try:
    while True:
        # se a posição mudou (usuário mexeu), encerra
        current_pos = gui.position()
        if current_pos != last_pos:
            print("Detectado movimento manual. Encerrando...")
            break

        # movimenta o mouse levemente (vai e volta)
        gui.moveRel(50, 0, duration=0.5)
        gui.moveRel(-50, 0, duration=0.5)

        # atualiza última posição controlada
        last_pos = gui.position()

        time.sleep(2)

except KeyboardInterrupt:
    print("Interrompido pelo usuário (CTRL+C).")

#gui.scroll(500)#UP
#gui.mouseUp(100,100, button="left") #mouse movimenta para com o botão pressionado
#gui.click(500, 500, 3, 3, button="left") #tem o double e triple também