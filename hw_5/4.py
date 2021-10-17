# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("4", "r", encoding='utf-8') as file:
    lines = file.readlines()
    new_str = ''
    for line in lines:
        new_str += line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')

with open("4ru", "w", encoding='utf-8') as file:
    file.write(new_str)
