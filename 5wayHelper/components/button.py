import pygetwindow
import keyboard
import time

def activate_game_window():
    game_window = pygetwindow.getWindowsWithTitle('Path of Exile')[0]
    game_window.activate()  # Активировать окно игры

def action_for_button_1():
    activate_game_window()
    keyboard.send('enter')  
    keyboard.press_and_release('ctrl+a')
    keyboard.send('enter')  
    time.sleep(1)
    keyboard.send('enter')  
    keyboard.write('%RULES 5way ::: DONT EXIT map if YOU DIE. NOT ENTER into THE BIG PURPLE CIRCLE. DONT ATTACK MOBS. Not open TP in this MAP. Remove ALL THE ITEMS AND EFFECTS THAT PROHIBIT YOUR HERO FROM HAVING AN ENERGY SHIELD. Del you PORTAL skil in YOU GEAR ( CWDT + PORTAL ). Equip CHAOS resist = 75%. AND have HP 3000+, Have Regeneration HP, Delete ALL Destructive EFFECTS Loss REGENERATION you HP. check you all res = 75%.')  
    keyboard.send('enter')  
    time.sleep(3)

def action_for_button_2():
    activate_game_window()
    keyboard.send('enter')  
    keyboard.press_and_release('ctrl+a')
    keyboard.send('enter')  
    time.sleep(1)
    keyboard.send('enter')  
    keyboard.write('%правила 5-вау: 1) НЕЛЬЗЯ ВЫХОДИТЬ С КАРТЫ ЕСЛИ СДОХ 2) Нельзя бить мобов на карте 3) Нельзя ходить по карте, надо стоять 4) Нельзя ставить ТП на карте, оно внизу уже стоит 5) В конце таймера вверху экрана выходим с карты (тп внизу).')  
    keyboard.send('enter')  
    time.sleep(2)
    keyboard.send('enter')
    keyboard.write('%ПРОВЕРЬТЕ ХАОС РЕЗ 75 % + ВКЛЮЧЁННЫЙ РЕГЕН ХП + ОТСУТСТВИЕ ВЕЩЕЙ И ПАССИВОК НА ЗАПРЕТ РЕГЕНА ХП.')
    keyboard.send('enter')
    time.sleep(2)
    keyboard.send('enter') 
    keyboard.write('%Если умер не выходи с карты до конца таймера вверху! Чтобы выжить - Стой AFK, имей 75% резиста к хаосу, и 3000 HP. Не атакуй мобов. Не призывай миньонов, тотемы. Не входи в фиолетовый круг!') 
    keyboard.send('enter')
    time.sleep(3)

def action_for_button_3():
    activate_game_window()
    keyboard.send('enter')  
    keyboard.press_and_release('ctrl+a')
    keyboard.send('enter')  
    time.sleep(1)
    keyboard.send('enter')  
    keyboard.write('%Привет')  
    keyboard.send('enter')  
    time.sleep(3)

def action_for_button_4():
    activate_game_window()
    keyboard.send('enter')  
    keyboard.press_and_release('ctrl+a')
    keyboard.send('enter')  
    time.sleep(1)
    keyboard.send('enter')  
    keyboard.write('%If you like the service, you can send me vouches. channel on TFT => "Service Voucher" => write => "5 Way Carry @deadyeas" <3')  
    keyboard.send('enter')  
    time.sleep(3)
