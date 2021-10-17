# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("2", "r", encoding='utf-8') as file:
    my_lines = file.readlines()
    print(f'В файле {len(my_lines)} строк')
    for i, line in enumerate(my_lines):
        print(f'В строке {i + 1} {len(line.split())} слов(а)')
