import keyboard
import pygetwindow
import time
import random
from components.setting import blacklist, diapason_ranges

def on_button_click(diapason_entry, text_entry):
    # Получаем значения из полей ввода
    diapason_value = int(diapason_entry.get())
    text_value = text_entry.get()

    # Добавляем ваш код
    game_window = pygetwindow.getWindowsWithTitle('Path of Exile')[0]
    game_window.activate()  # Активировать окно игры

    for trade_channel in [820, 1055, 1, 5550, 5055]:  # Проходим по каждому каналу
        keyboard.send('enter')  # Нажать клавишу Enter
        keyboard.press_and_release('ctrl+a')
        keyboard.write(f'/trade {trade_channel} en') 
        keyboard.send('enter')  # Нажать клавишу Enter
        time.sleep(1)
        keyboard.send('enter')  # Нажать клавишу Enter
        keyboard.write('$' + text_value)  # Эмулировать ввод текста из поля "Текст"
        keyboard.send('enter')  # Нажать клавишу Enter
        time.sleep(3)

    for _ in range(diapason_value):
        # Выбираем случайный диапазон из списка
        start_range, end_range = random.choice(diapason_ranges)

        # Генерируем уникальное случайное число в диапазоне, избегая чёрного списка
        random_number = random.randint(start_range, end_range)
        while random_number in blacklist:
            random_number = random.randint(start_range, end_range)

        # Добавляем сгенерированное число в чёрный список
        blacklist.add(random_number)

        keyboard.send('enter')  # Нажать клавишу Enter
        keyboard.press_and_release('ctrl+a')
        keyboard.write(f'/trade {random_number} ru') 
        keyboard.send('enter')  # Нажать клавишу Enter
        time.sleep(1)
        keyboard.send('enter')  # Нажать клавишу Enter
        keyboard.write('$' + text_value)  # Эмулировать ввод текста из поля "Текст"
        keyboard.send('enter')  # Нажать клавишу Enter
        time.sleep(3)