# 2) Создать текстовый файл(не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("task2.txt", "r", encoding="utf-8") as read_file:
    content = read_file.readlines()
    for num, line in enumerate(content):
        print(f"В строке {num + 1}: {len(line.split())} слов(а)")
    print(f"Всего: {len(content)} строк(и)\n")
