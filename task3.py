# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("task3.txt", "r", encoding="utf-8") as read_file:
    content = read_file.readlines()
    salary = 0
    my_list = []
    for line in content:
        my_list = list(line.split())
        salary += float(my_list[1])
        if float(my_list[1]) < 20000:
            print(f' Зарплата меньше 20 тыс у {my_list[0]}a')
    print(f'Средняя величина дохода = {salary / len(content)}')
