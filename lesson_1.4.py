from sys import argv
from functools import reduce
from itertools import count, cycle
"""
    1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
# script, hours, money_per_hour, bonus = argv
# def task_1():
#     def calс_salary(hours, money_per_hour, bonus):
#         try:
#             result = (int() * float(money_per_hour)) + float(bonus)
#         except ValueError:
#             return
#         return result
#
#     print(calс_salary(hours, money_per_hour, bonus))
"""
    2. Представлен список чисел. Необходимо вывести элементы исходного списка,
    значения которых больше предыдущего элемента.
    Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
    Для формирования списка использовать генератор.
    Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
    Результат: [12, 44, 4, 10, 78, 123].
"""
def task_2():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    list_result = [k for i, j in enumerate(my_list) for k in my_list[i + 1:i + 2] if k > j]
    print(list_result)
"""
    3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
    Необходимо решить задание в одну строку.
    Подсказка: использовать функцию range() и генератор.
"""
def task_3():
    print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])
"""
    4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
    Сформировать итоговый массив чисел, соответствующих требованию.
    Элементы вывести в порядке их следования в исходном списке.
    Для выполнения задания обязательно использовать генератор.
    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
    Результат: [23, 1, 3, 10, 4, 11]
"""
def task_4():
    def my_counter(lst: list) -> dict:
        result = {}
        for key, value in enumerate(lst):
            if result.get(value) is None:
                result[value] = 1
            else:
                result[value] += 1
        return result

    my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    counter = my_counter(my_list)
    list_res = [x for x, n in counter.items() if n == 1]
    print(list_res)
"""
    5. Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы).
    Необходимо получить результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce().
"""
def task_5():
    def multiplication(prev_el, el):
        print(el, prev_el)
        return prev_el * el

    print(reduce(multiplication, [i for i in range(100, 1001) if i % 2 == 0]))
"""
    6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools.
    Обратите внимание, что создаваемый цикл не должен быть бесконечным.
    Необходимо предусмотреть условие его завершения.
    Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
def task_6():
    print("Итератор,count:")
    for item in count(2):
        if item > 10:
            break
        else:
            print(item)

    print("\nИтератор, cycle:")
    i = 0
    for value in cycle([1, 2, 3]):
        if i > 10:
            break
        print(value)
        i += 1
"""
    7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    При вызове функции должен создаваться объект-генератор.
    Функция должна вызываться следующим образом: for el in fact(n).
    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
    начиная с 1! и до n!.
    Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
def task_7():
    print("Factorial:")
    def fact(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
            yield result

    for el in fact(10):
        print(el)
if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
