# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('task5.txt', 'w', encoding="utf-8") as f_obj:
    print("Введите набор чисел, разделенные пробелами: ")
    text = input()
    f_obj.write(text + '\n')

with open('task5.txt', 'r', encoding="utf-8") as f_obj:
    content = f_obj.read()
    print(content)
    my_list = content.split()
    result = 0
    for el in my_list:
        result += int(el)
    print("Сумма чисел в файле =", result)
