"""
    1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
    в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода.
    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
"""
def task_1():
    import re

    class Date:
        max_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        max_days_in_month_ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def __init__(self, date_string):
            match_result = re.match(r'^\d\d-\d\d-\d\d\d\d$', date_string)
            if match_result is None:
                raise Exception(f"{date_string} - incorrect date format, use dd-mm-yyyy format")
            self.date_string = date_string
            self.day, self.month, self.year = map(int, date_string.split('-'))

        @classmethod
        def extract(cls, date_string):
            date = cls(date_string)
            return [date.day, date.month, date.year]

        @staticmethod
        def validate(date_string):
            date = Date(date_string)
            is_not_zero = date.day > 0 and date.month > 0 and date.year > 0
            if date.year % 4 == 0 and date.year % 100 != 0 or date.year % 400 == 0:
                is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month_ly[date.month - 1]
            else:
                is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month[date.month - 1]
            return is_not_zero and is_fit_boundaries

    real_date_str = '22-12-1983'
    not_valid_date_str = '29-02-2019'
    incorrect_date_str = '9-02/*019'

    real_date = Date(real_date_str)
    print(f"{real_date.extract(real_date_str)} - extracted numbers")

    not_valid_date = Date(not_valid_date_str)
    print(f"{real_date.extract(not_valid_date_str)} - extracted numbers")

    try:
        incorrect_date = Date(incorrect_date_str)
    except Exception as e:
        print(e)

    if Date.validate(real_date_str):
        print(f"{real_date_str} - valid date")
    else:
        print(f"{real_date_str} - invalid date")

    if Date.validate(not_valid_date_str):
        print(f"{not_valid_date_str} - valid date")
    else:
        print(f"{not_valid_date_str} - invalid date")
"""
    2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
    вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
    эту ситуацию и не завершиться с ошибкой.
"""
def task_2():
    class DivisionByZeroError(Exception):
        def __init__(self, txt):
            self.txt = txt


    def smart_divider(a, b):
        if b == 0:
            raise DivisionByZeroError(f'{a} / {b} = Division By Zero Error!')
        return a / b


    try:
        smart_divider(6, 0)
    except DivisionByZeroError as e:
        print(e)

    print(f"45 / 5 = {smart_divider(45, 5)}")
"""
    3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
    Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
    Класс-исключение должен контролировать типы данных элементов списка.
    Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам
    не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
    сформированный список выводится на экран.
    Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
    При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
    только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
    отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
def task_3():
    class NaNError(Exception):
        def __init__(self, txt):
            self.txt = txt

    def number_filter(string):
        if string.isdigit():
            return string
        else:
            try:
                float(string)
                return string
            except ValueError:
                raise NaNError(f'Error: {string} - is not a number')

    input_txt = ''
    counter = 1
    numbers_list = []
    print("Введите числа по одному, для выхода введите 'stop'")
    while input_txt != 'stop':
        try:
            input_txt = input(f"{counter}: ")
            numbers_list.append(number_filter(input_txt))
            counter += 1
        except NaNError as e:
            if input_txt != 'stop':
                print(e.txt)

    print(f"Result list:\n{numbers_list}")
"""
    4. Начните работу над проектом «Склад оргтехники».
    Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов.
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
    5. Продолжить работу над первым заданием.
    Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
    Для хранения данных о наименовании и количестве единиц оргтехники,
    а также других данных, можно использовать любую подходящую структуру, например словарь.
    6. Продолжить работу над вторым заданием.
    Реализуйте механизм валидации вводимых пользователем данных.
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
    изученных на уроках по ООП.
"""
def task_4_5_6():
    class Warehouse:
        __storage = []
        __summary = {}

        def push(self, equipment):
            if not isinstance(equipment, OfficeEquipment):
                raise Exception('Склад может принимать только оргтехнику')
            self.__storage.append(equipment)
            if self.__summary.get(equipment.type) is not None:
                self.__summary[equipment.type] += 1
            else:
                self.__summary.setdefault(equipment.type, 1)

        def report_items(self):
            for item in self.__storage:
                print(item)

        def report_total(self):
            for k, v in self.__summary.items():
                print(f'{k}: {v} шт')

    class OfficeEquipment:
        def __init__(self, type: str, model: str, cost: float, sn: str):
            self.type = str(type)
            self.model = str(model)
            self.cost = float(cost)
            self.sn = str(sn)

        def __str__(self):
            return f"{self.type} {self.model}"

    class Printer(OfficeEquipment):
        def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
            self.is_colorful = is_colorful
            super().__init__('Принтер', model, cost, sn)

    class Scanner(OfficeEquipment):
        def __init__(self, model: str, cost: float, dpi: str, sn: str):
            self.dpi = dpi
            super().__init__('Сканер', model, cost, sn)

    class Copier(OfficeEquipment):
        def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
            self.is_colorful = is_colorful
            self.dpi = dpi
            self.velocity = velocity
            super().__init__('МФУ', model, cost, sn)

    printer01 = Printer('Epson L120', 7300.12, True, 'N6SS549876548')
    printer02 = Printer('HP Laser 107a', 6600, False, 'FG64855SFG5')
    scanner01 = Scanner('Epson Perf V19', 5010, '4800x4800', '65482321FF5')
    scanner02 = Scanner('Canon LiDE 300', 4700.45, '2400x2400', '31313131FFF')
    copier01 = Copier('Canon PIXMA MG2540S', 2299.73, True, '4800x600', 8, 'FG8#HHHF')
    copier02 = Copier('Brother MFC-L2720DWR', 19100, False, '2400x600', 30, '9BB654852133')
    copier03 = Copier('HP LaserJet M132nw', 14604.20, False, '1200x1200', 22, '9BB654848554')

    warehouse = Warehouse()
    warehouse.push(printer01)
    warehouse.push(printer02)
    warehouse.push(scanner01)
    warehouse.push(scanner02)
    warehouse.push(copier01)
    warehouse.push(copier02)
    warehouse.push(copier03)

    warehouse.report_items()
    warehouse.report_total()
"""
    7. Реализовать проект «Операции с комплексными числами».
    Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
    Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
    выполнив сложение и умножение созданных экземпляров.
    Проверьте корректность полученного результата.
"""
def task_7():
    class ComplexNumber:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __add__(self, other):
            a = self.a + other.a
            b = self.b + other.b
            return ComplexNumber(a, b)

        def __mul__(self, other):
            a = (self.a * other.a) - (self.b * other.b)
            b = (self.a * other.b) + (self.b * other.a)
            return ComplexNumber(a, b)

        def __str__(self):
            return f'{self.a} + {self.b}i'

    z1 = ComplexNumber(2, 5)
    z2 = ComplexNumber(3, 6)
    z3 = z1 + z2
    z4 = z1 * z2

    print(f'z1 = {z1}')  # z1 = 2 + 5i
    print(f'z2 = {z2}')  # z2 = 3 + 6i
    print(f'z1 + z2 = {z3}')  # z1 + z2 = 5 + 11i
    print(f'z1 * z2 = {z4}')  # z1 * z2 = -24 + 27i
if __name__ == "__main__":
    #task_1()
    #task_2()
    #task_3()
    #task_4_5_6()
    task_7()