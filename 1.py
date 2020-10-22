# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

from random import randint

class LotoCard:
    def __init__(self, player_name):
        self.player_name = player_name
        self.card = self.__card_generate()

    def __str__(self):
        return '\n'.join(' '.join([str(card_elem) for card_elem in card_str]) for card_str in self.card)

    def __card_generate(self):
        card = [['', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '']]
        for i, card_str in enumerate(card):
            for ii, card_elem in enumerate(card_str):
                if randint(0, 1) == 1:
                    card[i][ii] = randint(1, 90)
                    while sum([element.count(card[i][ii]) for element in card]) > 1:
                        card[i][ii] = randint(1, 90)
        return card

    def __sub__(self, other):
        for i, card_str in enumerate(self.card):
            for ii, card_elem in enumerate(card_str):
                if self.card[i][ii] == other:
                    self.card[i][ii] = '-'

    def __eq__(self, other):
        return sum([element.count(other) for element in self.card]) > 0

    def count(self):
        return sum([sum([1 if element != '' and element != '-' else 0 for element in row_element]) for row_element in self.card])


class LotoGame:
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player
        self.barrels = [num for num in range(1, 91)]
        print(self.barrels)

    def start(self):
        while True:
            barrel = self.barrels.pop(randint(0, len(self.barrels) - 1))
            print(
                f'Новый бочонок: {barrel} (осталось {len(self.barrels)})')
            print('------ Ваша карточка -----\n' + str(self.human_player) + \
                  '\n--------------------------\n-- Карточка компьютера ---\n' \
                  + str(self.computer_player) + '\n--------------------------')
            answer = str(input('Зачеркнуть цифру? (y/n) ')).lower()
            if (answer == 'n' and human_player == barrel) or (answer == 'y' and human_player != barrel):
                print('Вы проиграли, введено неправильное действие.')
                break
            elif (randint(0, 1000) == 0):
                print('Робот проиграл, введено неправильное действие.')
                break
            else:
                human_player - barrel
                computer_player - barrel


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame(human_player, computer_player)
game.start()
