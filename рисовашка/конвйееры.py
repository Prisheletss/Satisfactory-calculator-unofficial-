"""
============================================================================================================================================================================================================================================
ТЕХНИЧЕСКИЕ ШТУЧКИ                                                                                   ТЕХНИЧЕСКИЕ ШТУЧКИ                                                                                                  ТЕХНИЧЕСКИЕ ШТУЧКИ
============================================================================================================================================================================================================================================
"""

# моды ===== ===== ===== ===== =====
import pygame as pygame  # пугаме
from pygame.locals import *  # кнопочки
import random  # рандом
from PIL import Image, ImageChops # обработка изображений
import os # работа с системой компа
import math
import datetime

# ===== ===== ===== ===== ===== =====


# тех момент ===== ===== ===== ===== ===== ===== =====
pygame.init()  # разрешаем доступ к пугаму
window = pygame.display.set_mode((1650, 900))  # окошко
#window_2 = pygame.display.set_mode((1650, 900))
window.fill((255, 255, 255))  # рисуем окошко
pygame.display.update()  # обновляем моник
stile = pygame.font.Font(None, 60) # создаём свой шрифт
# ===== ===== ===== ===== ===== ===== ===== ===== =====



"""
============================================================================================================================================================================================================================================
КЛАССОВЫЕ ЭЛЕМЕНТЫ                                                                                   КЛАССОВЫЕ ЭЛЕМЕНТЫ                                                                                                  КЛАССОВЫЕ ЭЛЕМЕНТЫ
============================================================================================================================================================================================================================================
"""


# класс картинок ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
class PNG():
    def __init__(self, x_on_monitor, y_on_monitor, width, height, png_name, unicuie_name, x_on_png, y_on_png, scale = 1, rotate = 0, mirrored = [False, False]):
        self.x = x_on_monitor  # левая грань
        self.y = y_on_monitor  # верхняя грань
        self.width = width  # ширина картинки
        self.height = height  # высота картинки
        self.png_name = png_name  # имя картинки
        self.scale = scale
        self.rotate = rotate
        self.x_on_png = x_on_png
        self.y_on_png = y_on_png
        self.unicuie_name = unicuie_name  # название объекта
        self.x_mirrored = mirrored[0]
        self.y_mirrored = mirrored[1]
        
        self.surf = pygame.image.load(png_name)
        self.surf = pygame.transform.flip(self.surf, mirrored[0], mirrored[1])
        self.surf = pygame.transform.rotate(self.surf, rotate)
        self.cords = self.surf.get_rect(bottomright=(width+x_on_monitor, height+y_on_monitor))
        self.rect = pygame.Rect(x_on_png, y_on_png, width, height)
        self.subscreen = self.surf.subsurface(self.rect)

    def draw(self, display=window):  # нарисовать
        display.blit(self.subscreen, self.cords)


# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====


# класс кнопок ===== ===== =====  ===== ===== ===== ===== ===== ===== ===== =====
class Button():
    def __init__(self, x_on_monitor, y_on_monitor, width, height, png_name, unicuie_name, x_on_png, y_on_png, scale = 1, rotate = 0):
        self.png = PNG(x_on_monitor, y_on_monitor, width, height, png_name, unicuie_name, x_on_png, y_on_png, scale = 1, rotate = 0)  # изображение кнопки
        self.x = x_on_monitor  # левая грань
        self.y = y_on_monitor  # верхняя грань
        self.name = unicuie_name  # имя кнопки
        self.width = width  # ширина кнопки
        self.height = height  # высота кнопки

    def pressed(self, click):  # возвращает 1 если кнопка нажата. иначе-0
        if (click[0] in range(self.x, self.x+self.width)) and (click[1] in range(self.y, self.y+self.height)): return True
        else: return False

    def draw(self):  # рисует кнопку
        self.png.draw(window)
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====




"""
============================================================================================================================================================================================================================================
ФУКЦИИ                                                                                                     ФУКЦИИ                                                                                                                     ФУКЦИИ
============================================================================================================================================================================================================================================
"""



# ================= =============== ВЫБОР НАЖАТОЙ КНОПКИ =============== =================
def button_select(button_list, mouse): # возвращает нажатую кнопку. если таковой нет - 'no'
    #print(button_list)
    for i_0001 in button_list: # проверяем факт нажатия кнопок
        if i_0001.pressed(mouse): return i_0001; break # если мышь в месте этой кнопки, то возвращаем кнопку
    else: return 'no' # если таких кнопок не нашлось
# ================= ================= ================= ================= =================



# ============ КАКАЯ КЛАВИША НАЖАТА ============
def returner():
    keys = pygame.key.get_pressed()
    #print(keys)
    if keys[pygame.K_1]: return '1'
    elif keys[pygame.K_2]: return '2'
    elif keys[pygame.K_3]: return '3'
    elif keys[pygame.K_4]: return '4'
    elif keys[pygame.K_5]: return '5'
    elif keys[pygame.K_6]: return '6'
    elif keys[pygame.K_7]: return '7'
    elif keys[pygame.K_8]: return '8'
    elif keys[pygame.K_9]: return '9'
    elif keys[pygame.K_0]: return '0'

    elif keys[pygame.K_RETURN]: return 'enter'
    elif keys[pygame.K_BACKSPACE]: return 'delete'

    elif keys[pygame.K_RIGHT]: return 'right'
    elif keys[pygame.K_LEFT]: return 'left'
    elif keys[pygame.K_UP]: return 'up'
    elif keys[pygame.K_DOWN]: return 'down'
    
    else: return 'no'
# =============== =============== ===============



# =============== =============== ИЗМЕНЕНИЕ ТЕКСТА ============== ===============
def text_edit(text, is_selected):
    returned = returner()
    if returned != 'no':
        if (returned != 'enter') and (returned != 'delete'): text += returned
        elif returned == 'delete': text = (text[0:-1] if len(text) > 1 else '')
        else: is_selected = ''
    return (text, is_selected)
# =============== =============== ============== =============== ===============



# ==================  ================= генератор имени ================= ==================
def name_generator(letters, numbers): # создаёт случайное сочетание из букв и цыфр, по их заданному числу
    name_out = '' # имя
    for i_0002 in range(letters):
        name_out += str(chr(random.randint(97, 122))) # добавляем буквы
    if numbers > 0: name_out += '_'
    for i_0003 in range(numbers):
        name_out += str(random.randint(0,9)) # добавляем цифры
    return name_out # возвращааем имя
# ================= ================= ================= ================= =================



#
def place(kind, x, y, rotate = 0, mirrored = [False, False]):
    PNG(3101+x*50, 5601-y*50, 49, 49, kind+'.png', name_generator(10,10), 0, 0, 1, rotate, mirrored).draw(window_2)
#



#
def place_2(a, x=0, y=0, rotate=1, modder=1):
    place('разделитель', x, y)
    #print(a)
    i_0004 = 0
    while i_0004 < a*modder:
        place('конвейер', x+rotate*(1+i_0004), y, -90*rotate)
        i_0004 += 1
    if i_0004 == 0:
        place('поворот', x+rotate, y, -90*rotate, [False if (rotate == 1) else True, False])
        place('конвейер', x+rotate, y+1)
    else:
        place('поворот', x+rotate*(1+i_0004), y, -90*rotate, [False if (rotate == 1) else True, False])
        place('конвейер', x+rotate*(1+i_0004), y+1)
    place('конвейер', x, y+1)
#



#
def output_2(log=2, x=0, y=0, modder=1):
    output_number = 2**log
    place('конвейер', x, y)
    place('разделитель', x, y+1)
    c_008 = 0
    while c_008 < (output_number//2 - 1)*(modder//2-(modder//log)-1):
        place('конвейер', x-1-c_008, y+1, 90)
        place('конвейер', x+1+c_008, y+1, -90)
        c_008 += 1
    if c_008 == 0:
        place('поворот', x-1, y+1, 90, [True, False])
        place('поворот', x+1, y+1, -90)
    else:
        place('поворот', x-1-c_008, y+1, 90, [True, False])
        place('поворот', x+1+c_008, y+1, -90)
    a = 0
    for a in range(log - 1):
        b = 0
        for b in range(2**a):
            place_2(output_number//(2**(2+a))-1, x-1-c_008+b*output_number//(2**(1+a)), y+2+2*a, 1, (modder+1)*2)
            place_2(output_number//(2**(2+a))-1, x+1+c_008-b*output_number//(2**(1+a)), y+2+2*a, -1, (modder+1)*2)
        if b == 0:
            place_2(output_number//4-1, x-1-c_008, y+2, 1, (modder+1)*2)
            place_2(output_number//4-1, x+1+c_008, y+2, -1, (modder+1)*2)
#



#
def place_3(a, x=0, y=0):
    place('разделитель', x, y)
    i_0005 = 0
    while i_0005 < a:
        place('конвейер', x+1+i_0005, y, -90)
        place('конвейер', x-1-i_0005, y, 90)
        i_0005 += 1
    if i_0005 == 0:
        place('поворот', x+1, y, -90)
        place('конвейер', x+1, y+1)
        place('поворот', x-1, y, 90, [True, False])
        place('конвейер', x-1, y+1)
    else:
        place('поворот', x+1+i_0005, y, -90)
        place('конвейер', x+1+i_0005, y+1)
        place('поворот', x-1-i_0005, y, 90, [True, False])
        place('конвейер', x-1-i_0005, y+1)
    place('конвейер', x, y+1)
#



#
def output_3(log=2, x=0, y=0, modder=1,):
    output = 3**log
    place('конвейер', x, y)
    place('разделитель', x, y+1)
    c_009 = 0
    while c_009 < (output//3 - 1):#*modder:
        place('конвейер', x-1-c_009, y+1, 90)
        place('конвейер', x+1+c_009, y+1, -90)
        c_009 += 1

    if c_009 == 0:
        place('конвейер', x-1, y+2)
        place('поворот', x-1, y+1, 90, [True, False])
        place('конвейер', x+1, y+2)
        place('поворот', x+1, y+1, -90)
    else:
        place('конвейер', x-1-c_009, y+2)
        place('поворот', x-1-c_009, y+1, 90, [True, False])
        place('конвейер', x+1+c_009, y+2)
        place('поворот', x+1+c_009, y+1, -90)
    place('конвейер', x, y+2)
    a = 0
    for a in range(log - 1):
        b = 0
        for b in range(3**a):
            place_3(output//(3**(2+a))-1, x-1-c_009+b*output//(3**(1+a)), y+3+2*a)
            place_3(output//(3**(2+a))-1, x+1+c_009-b*output//(3**(1+a)), y+3+2*a)
            place_3(output//(3**(2+a))-1, x, y+3+2*a)
        if output != 81:
            place_3(output//(3**(2+a))-1, x+1+c_009+(b-1)*output//(3**(1+a)), y+3+2*a)
            place_3(output//(3**(2+a))-1, x-1-c_009-(b-1)*output//(3**(1+a)), y+3+2*a)
    if output == 81:
        place_3(2, x-36, y+5)
        place_3(2, x+36, y+5)
        for c_010 in range(27):
            place_3(0, x-39+3*c_010, y+3+2*a)
#


"""
============================================================================================================================================================================================================================================
ГЛАВНЫЙ ЦЫКЛ                                                                                            ГЛАВНЫЙ ЦЫКЛ                                                                                                           ГЛАВНЫЙ ЦЫКЛ
============================================================================================================================================================================================================================================
"""



button_input_number = Button(590, 0, 200, 100, 'входы.png', 'button_input_number', 0, 0)
button_output_number = Button(810, 0, 200, 100, 'выходы.png', 'button_output_number', 0, 0)
buton_NEXT = Button(750, 110, 100, 100, 'готово.png', 'buton_NEXT', 0, 0)
input_number = ''
output_number = ''
list_inputs = []
list_only_inputs = []
list_outputs = []
list_only_outputs = []
stage = 0
write = False
#button_list
is_selected = ''
button_equal = Button(1030, 20, 150, 67, 'выкл.png', 'buton_выкл', 0, 0)
png_equal = PNG(1030, 20, 150, 67, 'вкл.png', 'png_вкл', 0, 0)
equal = False
list_buttons = []

run = True
while run:
    if stage == 0:
        for event in pygame.event.get(): # проверка нажатия клавишь
            if event.type == pygame.QUIT: 
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouse = [mouse_x, mouse_y]
                if event.button == 1:
                    if (len(input_number) > 0) and (len(output_number) > 0) and buton_NEXT.pressed(mouse): is_selected = 'NEXT'
                    elif button_input_number.pressed(mouse): is_selected = 'input'
                    elif button_output_number.pressed(mouse): is_selected = 'output'
                    elif button_equal.pressed(mouse):
                        equal = not equal
                        is_selected = ''
                    else: is_selected = ''

        if is_selected == 'input':
            (input_number, is_selected) = text_edit(input_number, is_selected)
        elif is_selected == 'output':
            (output_number, is_selected) = text_edit(output_number, is_selected)
        elif is_selected == 'NEXT':
            stage = 1
            ready = 0
            for c_0000 in range(int(input_number)):
                button = Button(10, 110*c_0000, 364, 100, 'ввод.png', 'input'+str(c_0000), 0, 0)
                list_inputs.append(['', button, (35, button.y + 40)])
                list_buttons.append(button)
                list_only_inputs.append(button)
            for c_0001 in range(int(output_number)):
                button = Button(1276, 110*c_0001, 364, 100, 'ввод.png', 'input'+str(c_0001), 0, 0)
                list_outputs.append(['', button, (1299, button.y + 40)])
                list_buttons.append(button)
                list_only_outputs.append(button)
                

        button_input_number.draw()
        button_output_number.draw()
        text1 = stile.render(input_number, True, (0,0,0))
        text2 = stile.render(output_number, True, (0,0,0))
        window.blit(text1, (642,40)) #len(input_number)*29,40))
        window.blit(text2, (862, 40)) #-len(output_number)*29,40))
        button_equal.draw()
        if equal: png_equal.draw()
        
        if (len(input_number) > 0) and (len(output_number) > 0): buton_NEXT.draw()
        
        pygame.display.update()
        window.fill((255, 255, 255)) # рисуем окошко
        pygame.time.delay(130)

    if stage == 1:
        for event in pygame.event.get(): # проверка нажатия клавишь
            if event.type == pygame.QUIT: 
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouse = [mouse_x, mouse_y]
                if event.button == 1:
                    if ready == len(list_buttons):
                        button = button_select(list_buttons+[buton_NEXT], mouse)
                        if button != 'no':
                            is_selected = button
                            if is_selected == buton_NEXT: run = False
                            
                    else:
                        button = button_select(list_buttons, mouse)
                        if button != 'no':
                            is_selected = button
                #elif event.button == 3: run = False
                    
        if is_selected in list_only_inputs:
            num = list_only_inputs.index(is_selected)
            (list_inputs[num][0], is_selected) = text_edit(list_inputs[num][0], is_selected)        
        elif (is_selected in list_only_outputs) and (not equal):
            num = list_only_outputs.index(is_selected)
            (list_outputs[num][0], is_selected) = text_edit(list_outputs[num][0], is_selected)
        
        button_input_number.draw()
        button_output_number.draw()
        text1 = stile.render(input_number, True, (0,0,0))
        text2 = stile.render(output_number, True, (0,0,0))
        window.blit(text1, (642,40)) #len(input_number)*29,40))
        window.blit(text2, (862, 40)) #-len(output_number)*29,40))
        
        #print(ready, len(list_buttons))
        if ready < len(list_buttons): ready = 0
        elif ready >= len(list_buttons): buton_NEXT.draw()
        #buton_NEXT.draw()
        button_equal.draw()
        if equal: png_equal.draw()

        ready = 0
        summ = 0
        
        for c_0002 in list_inputs:
            c_0002[1].draw()
            
            try: summ += int(c_0002[0])
            except: ValueError
            
            text_n = stile.render(c_0002[0], True, (0,0,0))
            window.blit(text_n, c_0002[2])
            if len(c_0002[0]) > 0: ready += 1
        #print(summ)
        for c_0003 in list_outputs:
            c_0003[1].draw()
            if equal: c_0003[0] = str(summ/len(list_outputs))
            text_n = stile.render(c_0003[0], True, (0,0,0))
            window.blit(text_n, c_0003[2])
            if len(c_0003[0]) > 0: ready += 1
        
        pygame.display.update()
        window.fill((255, 255, 255)) # рисуем окошко
        pygame.time.delay(130)



"""
============================================================================================================================================================================================================================================
ПОСТОБРАБОТКА                                                                                           ПОСТОБРАБОТКА                                                                                                          ПОСТОБРАБОТКА
============================================================================================================================================================================================================================================
"""



inputs_list = [int(c_0004[0]) for c_0004 in list_inputs]
outputs_list = [int(c_0005[0][0:-2]) for c_0005 in list_outputs]
input_number = len(inputs_list)
monitor_x = 2300
monitor_y = 5100

window_2 = pygame.display.set_mode((6251, 6251))
PNG(0, 0, 6251, 6251, 'фон2.png', 'фон', 0, 0).draw(window_2)

if equal:
    written_type_of_output_number = [1]
    multipliers_of_output_number = [1]
    c_007 = 2
    output_number = len(outputs_list)
    number = len(outputs_list)
    while number != 1:
        if number % c_007 == 0:
            number = number//c_007
            written_type_of_output_number.append(c_007)
            if c_007 not in multipliers_of_output_number: multipliers_of_output_number.append(c_007)
        else:
            c_007 += 1
    if (len(multipliers_of_output_number) == 2) and (2 in multipliers_of_output_number): output_2(len(written_type_of_output_number)-1)     
    elif (len(multipliers_of_output_number) == 2) and (3 in multipliers_of_output_number): output_3(len(written_type_of_output_number)-1)
    elif (len(multipliers_of_output_number) == 3) and (2 in multipliers_of_output_number) and (3 in multipliers_of_output_number):
        output_2(written_type_of_output_number.count(2)+1, 0, 0, output_number)
        #for c_011 in range(written_type_of_output_number.count(3)):
            #output_2(written_type_of_output_number.count(2), )









   
pygame.display.update()
surf = pygame.Surface((6251, 6251))
surf.blit(window_2, (0, 0))
pygame.image.save(surf, 'avava.png')


                       

































