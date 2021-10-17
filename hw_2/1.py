# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

our_list = [1, 'text', ('t', 'upl', 'e'), 555, {'text': '1', 'dig': 2}]
check_tuple = ("<class 'int'>", "<class 'str'>", "<class 'tuple'>", "<class 'dict'>", "<class 'dict'>")

print(len(our_list))
for i in range(len(our_list)):
    if str(type(our_list[i])) == check_tuple[i]:
        print(f'Элемент {our_list[i]} действительно {check_tuple[i]}')
    else:
        print(f'Элемент {our_list[i]} не {check_tuple[i]}')
