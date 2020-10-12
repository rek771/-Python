# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        return self.name + ' go'

    def stop(self):
        return self.name + ' stoped'

    def turn(self, direction):
        if direction == 'left':
            return self.name + ' to left'
        elif direction == 'right':
            return self.name + ' to right'

    def show_speed(self):
        return self.name + ' ' + str(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return self.name + ' Превышение лимита 60 км/ч, скорость ' + str(self.speed)
        else:
            return self.name + ' ' + str(self.speed)


class SportCar(Car):
    def __init__(self, name, color, speed):
        super(SportCar, self).__init__(name, color, speed)


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return self.name + ' Превышение лимита 40 км/ч, скорость ' + str(self.speed)
        else:
            return self.name + ' ' + str(self.speed)


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super(PoliceCar, self).__init__(name, color, speed)
        self.is_police = True


town_car1 = TownCar('bug', 'red', 500)
town_car2 = TownCar('bug_new', 'red', 50)
sport_car = SportCar('porsche', 'white', 5000)
work_car1 = WorkCar('transporter', 'blue', 50)
work_car2 = WorkCar('gazel', 'brown', 30)
police_car = PoliceCar('Lamborghini', 'red', 30000)

print(town_car1.go())
print(town_car1.is_police)
print(town_car1.stop())
print(town_car1.turn('left'))
print(town_car1.turn('right'))
print(town_car1.show_speed())

print(town_car2.go())
print(town_car2.is_police)
print(town_car2.stop())
print(town_car2.turn('left'))
print(town_car2.turn('right'))
print(town_car2.show_speed())

print(sport_car.go())
print(sport_car.is_police)
print(sport_car.stop())
print(sport_car.turn('left'))
print(sport_car.turn('right'))
print(sport_car.show_speed())

print(work_car1.go())
print(work_car1.is_police)
print(work_car1.stop())
print(work_car1.turn('left'))
print(work_car1.turn('right'))
print(work_car1.show_speed())

print(work_car2.go())
print(work_car2.is_police)
print(work_car2.stop())
print(work_car2.turn('left'))
print(work_car2.turn('right'))
print(work_car2.show_speed())

print(police_car.go())
print(police_car.is_police)
print(police_car.stop())
print(police_car.turn('left'))
print(police_car.turn('right'))
print(police_car.show_speed())
