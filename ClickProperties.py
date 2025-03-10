import win32api, win32con
import time
import keyboard
import pyautogui

atualized_state = 0
counter = 0

def GetMultipleStates():
    left_press = win32api.GetKeyState(0x0001)   #Left Button == 0x001    State == -127 or -128 when pressed and State == 0 or 1 when released
    right_press = win32api.GetKeyState(0x0002)  #Right Button == 0x002    State == -127 or -128 when pressed and State == 0 or 1 when released
    wheel_press = win32api.GetKeyState(0x0002)  #Wheel Button == 0x004    State == -127 or -128 when pressed and State == 0 or 1 when released
    return left_press
    
while keyboard.is_pressed('q') == False:
    time.sleep(0.1)

    GetMultipleStates()
    if keyboard.is_pressed('c') == True:
        if counter >= 2:
            win32api.SetCursorPos( (x_inicial, y_inicial) )
        counter -= 3
    elif counter <= 0:
        print('Selecione dois cantos opostos:')
        counter = 1
    GetMultipleStates()
    elif ( left_press < 0 and left_press != atualized_state and counter == 1 ):
        atualized_state = left_press
        counter = 2
        x_inicial, y_inicial = win32api.GetCursorPos()
        print('Coordenadas selecionadas:    Xi = ', x_inicial, 'Yi = ', y_inicial)        
        print('Caso tenha selecionado errado, aperte [C]orrigir.\n')
    elif ( counter == 2):
        print('Selecione o canto inferior direito:')
        counter = 3
    elif ( left_press < 0 and left_press != atualized_state and counter == 3 ):
        counter = 4
        x_final, y_final = win32api.GetCursorPos()
        print('Coordenadas selecionadas:    Xf = ', x_final, 'Yf = ', y_final)
        print('Caso tenha selecionado errado, aperte [C]orrigir.\n')
    elif counter == 4:
        counter = 5
        delta_x = abs(x_final - x_inicial)
        delta_y = abs(y_final - y_inicial)
        x_inicial = min(x_final, x_inicial)
        y_inicial = min(y_final, y_inicial)
        im1 = pyautogui.screenshot(region=(x_inicial, y_inicial, delta_x, delta_y))
        im1.save(r'./savedimage.png')
        SavedPositions = open('SavedPositions.txt', 'w')
        text = ('Xi =' + chr(x_inicial) + 'Yi =' + chr(y_inicial) + 'Xf =' + chr(x_inicial + delta_x) + 'Yf =' + chr(y_inicial + delta_y))
    
        SavedPositions.write(text)
        SavedPositions.close()
        print('Imagem [',delta_x, 'x', delta_y, '] salva.')
        print('Xi =', x_inicial, 'Yi =', y_inicial, 'Xf =', (x_inicial + delta_x), 'Yf =', (y_inicial + delta_y))
        print('Caso tenha selecionado errado, aperte [C]orrigir.\n')
    
##pyautogui.displayMousePosition()
##X:  506 Y:  412 RGB: (  0,  34,  56)
##X: 1398 Y:  946 RGB: (  0,  34,  56)


