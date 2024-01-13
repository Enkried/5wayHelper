import tkinter as tk
from components.spammer import on_button_click
from components.button import action_for_button_1, action_for_button_2, action_for_button_3, action_for_button_4

# Создаем главное окно
root = tk.Tk()
root.title("Спамер PoE")

# Создаем и размещаем виджеты в окне
diapason_label = tk.Label(root, text="Диапазон:")
diapason_label.grid(row=0, column=0, padx=10, pady=10)

diapason_entry = tk.Entry(root)
diapason_entry.grid(row=0, column=1, padx=10, pady=10)

text_label = tk.Label(root, text="Текст:")
text_label.grid(row=1, column=0, padx=10, pady=10)

text_entry = tk.Entry(root)
text_entry.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(root, text="Начать спам", command=lambda: on_button_click(diapason_entry, text_entry))
button.grid(row=2, column=0, columnspan=2, pady=10)

button1 = tk.Button(root, text="Правила EN", command=action_for_button_1)
button1.grid(row=3, column=0, pady=10)

button2 = tk.Button(root, text="Правила RU", command=action_for_button_2)
button2.grid(row=3, column=1, pady=10)

button3 = tk.Button(root, text="Кнопка 3", command=action_for_button_3)
button3.grid(row=4, column=0, pady=10)

button4 = tk.Button(root, text="Отзыв", command=action_for_button_4)
button4.grid(row=4, column=1, pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()
