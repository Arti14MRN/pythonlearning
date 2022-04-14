"""
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов,
    и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
def task_1():
    from itertools import cycle
    from time import sleep

    class TrafficLight:
        __color = cycle([
            {'signal': 'red', 'duration': 7},
            {'signal': 'yellow', 'duration': 2},
            {'signal': 'green', 'duration': 4},
            {'signal': 'yellow', 'duration': 2}
        ])

        def running(self):
            light = next(self.__color)
            print(f"Сигнал {light['signal']}, пауза {light['duration']} сек.")
            sleep(light['duration'])


    traffic_light = TrafficLight()
    traffic_light.running()
    traffic_light.running()
    traffic_light.running()
    traffic_light.running()

"""
    2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
    Значения данных атрибутов должны передаваться при создании экземпляра класса.
    Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
    необходимого для покрытия всего дорожного полотна.
    Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
    толщиной в 1 см * число см толщины полотна.
    Проверить работу метода.
    Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

def task_2():
    class Road:
        def __init__(self, length: int, width: int):
            self._length = length
            self._width = width

        def get_mass(self, mass_1m2: int, thickness: int) -> int:
            '''
            Расчет массы асфальта
            :param mass_1m2: масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
            :param thickness: толщины полотна
            :return: масса асфальта в тоннах
            '''
            mass = self._length * self._width * mass_1m2 * thickness // 1000
            return mass

    road = Road(5000, 20)
    print(road.get_mass(25, 5) == 12500)
    print(road.get_mass(25, 5))

"""
    3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
    position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь,
    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
    дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров).
"""

def task_3():
    class Worker:
        def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {'wage': wage, 'bonus': bonus}


    class Position(Worker):
        def get_full_name(self):
            return f"{self.name} {self.surname}"

        def get_total_income(self):
            return sum(self._income.values())


    vasya = Position('user', 'superuser', 'programming', 100000, 20000)
    print(vasya.get_full_name())
    print(vasya.position)
    print(vasya.get_total_income())

"""
    4. Реализуйте базовый класс Car.
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
    40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов.
    Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

def task_4():

    class Car:
        def __init__(self, color: str, name: str, is_police: bool):
            self.speed = 0
            self.color = color
            self.name = name
            self.is_police = is_police

        def go(self, speed):
            self.speed = speed
            print(f'Разгоняемся до {speed} км/ч')

        def stop(self):
            self.speed = 0
            print('Останавливаемся')

        def turn(self, direction: str):
            if self.speed > 0:
                print(f'Поворачиваем {direction}')
            else:
                print('Не можем повернуть - мы стоим на месте')

        def show_speed(self):
            print(f'Скорость {self.speed} км/ч')


    class TownCar(Car):
        def __init__(self, color: str, name: str):
            self.speed = 0
            self.color = color
            self.name = name
            self.is_police = False

        def show_speed(self):
            if self.speed > 60:
                print(f'Внимание! Превышение скорости {self.speed} км/ч')
            else:
                print(f'Скорость {self.speed} км/ч')


    class SportCar(Car):
        def __init__(self, color: str, name: str):
            self.speed = 0
            self.color = color
            self.name = name
            self.is_police = False


    class WorkCar(Car):
        def __init__(self, color: str, name: str):
            self.speed = 0
            self.color = color
            self.name = name
            self.is_police = False

        def show_speed(self):
            if self.speed > 40:
                print(f'Внимание! Превышение скорости {self.speed} км/ч')
            else:
                print(f'Скорость {self.speed} км/ч')


    class PoliceCar(Car):
        def __init__(self, color: str, name: str):
            self.speed = 0
            self.color = color
            self.name = name
            self.is_police = True


    def test_drive(vehicle):
        print(f"Тест-драйв {'полицейского' if vehicle.is_police else 'гражданского'} автомобиля {vehicle.name}, цвет {vehicle.color}")
        vehicle.go(40)
        vehicle.show_speed()
        vehicle.turn('направо')
        vehicle.stop()
        vehicle.show_speed()
        vehicle.turn('налево')
        vehicle.go(60)
        vehicle.show_speed()
        vehicle.go(120)
        vehicle.show_speed()
        vehicle.stop()
        print("Тест-драйв окончен", end="\n\n")


    car = Car('белый', 'Kia Optima', False)
    test_drive(car)

    polo = TownCar('коричневый', 'Volkswagen Polo')
    test_drive(polo)

    veyron = SportCar('желтый', 'Bugatti Veyron')
    test_drive(veyron)

    largus = WorkCar('красный', 'Lada Largus')
    test_drive(largus)

    mondeo = PoliceCar('синий', 'Ford Mondeo')
    test_drive(mondeo)

"""
    5. Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка).
    Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

def task_5():
    class Stationery:
        def __init__(self, title):
            self.title = title

        def draw(self):
            print(f"Запуск отрисовки {self.title}")


    class Pen(Stationery):
        def draw(self):
            print(f"Запуск отрисовки ручкой {self.title}")


    class Pencil(Stationery):
        def draw(self):
            print(f"Запуск отрисовки карандашем {self.title}")


    class Handle(Stationery):
        def draw(self):
            print(f"Запуск отрисовки маркером {self.title}")


    stationery = Stationery('Гусиное перо')
    stationery.draw()

    pen = Pen('Гелевая')
    pen.draw()

    pencil = Pencil('Учебный')
    pencil.draw()

    handle = Handle('Для белой доски')
    handle.draw()

if __name__ == "__main__":
    task_1()
    #task_2()
    #task_3()
    #task_4()
    #task_5()
