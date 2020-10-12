# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("5", "w+", encoding='utf-8') as file:
    file.write(str(input('Введите числа через пробел: ')))
    file.seek(0)

    lines = file.readline().split()
    my_summ = 0
    for line in lines:
        my_summ += int(line)

print(my_summ)