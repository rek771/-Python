# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите кооличество секунд: '))

hours = seconds // 60 // 60
minutes = seconds // 60 - hours * 60
seconds = seconds - hours * 60 * 60 - minutes * 60
print(f'{hours}:{minutes}:{seconds}')
