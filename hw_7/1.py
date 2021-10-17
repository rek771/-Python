# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, own_list):
        self.own_list = own_list

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in col]) for col in self.own_list])

    def __add__(self, other):
        result = []
        if len(self.own_list) != len(other.own_list):
            print('Ошибка данных')
            return False
        for str1, str2 in zip(self.own_list, other.own_list):
            if len(str1) != len(str2):
                print('Ошибка данных')
                return False
            result.append([x + y for x, y in zip(str1, str2)])
        return Matrix(result)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])

print(matrix_1)
print(matrix_1 + matrix_2)
