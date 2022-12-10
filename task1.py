# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

with open("task1.txt", "w+", encoding="utf-8") as f_obj:
    while True:
        content = input('Введите данные:')
        if content == '':
            break
        f_obj.write(content)
    print(content)
