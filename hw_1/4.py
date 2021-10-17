# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число: '))
result = 0

while number > 0:
    dig = number % 10
    number = number // 10
    if dig > result:
        result = dig
    elif result == 9:
        break

print('В заданном числе максимальная цифра %d' % result)
