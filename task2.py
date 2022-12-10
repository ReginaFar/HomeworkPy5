# 2) Создать текстовый файл(не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("task2.txt", "w+", encoding="utf-8") as read_file:
    content = read_file.readlines()
    for word, line in enumerate(content):
        print(f"В строке {word + 1}: {len(line.split())} слов(а)")
    print(f"Всего: {len(content)} строк(и)\n")
