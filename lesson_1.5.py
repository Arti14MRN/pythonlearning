"""
    1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка.
"""
def task_1():
    input_not_empty = True
    file = open('task_1.txt', 'w', encoding='UTF-8')
    while input_not_empty:
        line = input()
        if line == '':
            input_not_empty = False
        else:
            file.write(line + '\n')
    file.close()
"""
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""
def task_2():
    with open('task_1.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        print(f"Всего строк: {len(lines)}")
        for key, value in enumerate(lines):
            words = value.split(' ')
            print(f"Слов в строке {key + 1}: {len(words)}")
"""
    3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
"""
def task_3():
    report = []
    sum_salaries = 0
    with open('task_1.txt', 'r', encoding='UTF-8') as file:
         rows = file.readlines()
         print("Оклады сотрудников")
         for row in rows:
             row_items = row.split(' ')
             report.append([row_items[0], int(row_items[1])])
             print(f"{row_items[0]}: {int(row_items[1])} руб.")
             sum_salaries += int(row_items[1])
    print("\nСотрудники с окладом менее 20000 руб.")
    [print(worker[0]) for worker in report if worker[1] < 20000]
    print(f"\nСредний оклад сотрудников {sum_salaries / len(report)} руб.")
"""
    4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
"""
def task_4():
    dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

    text_en = ''
    with open('task_1.txt', 'r', encoding='UTF-8') as file_en:
        text_en = file_en.read()

    text_ru = text_en
    for en, ru in dictionary.items():
        text_ru = text_ru.replace(en, ru)

    with open('task_1.tmp', 'w', encoding='UTF-8') as file_ru:
        file_ru.write(text_ru)
"""
    5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
def task_5():
    import random

    with open('task_7.txt', 'w', encoding='UTF-8') as file:
        splitter = ''
        for _ in range(5):
            file.write(splitter + str(random.randint(0, 10)))
            splitter = ' '

    with open('task_7.txt', 'r', encoding='UTF-8') as file:
        numbers_str = file.read()
        numbers_lst = numbers_str.split(' ')
        print(f"Содержимое файла:\n{numbers_str}")
        print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")
"""
    6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
    наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести словарь на экран.
    Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —
    Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
def task_6():
    import re

    report = {}
    with open('task_7.txt', 'r', encoding='UTF-8') as file:
        text = file.read()
        file.seek(0)
        for row in file:
            row_items = row.split(': ')
            hours = re.findall(r"\d+", row_items[1])
            report.update({row_items[0]: sum([int(i) for i in hours])})

    print(f"Исходный файл:\n{text}\n")
    print(f"Словарь:\n{report}")
"""
    7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
    название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
    Подсказка: использовать менеджеры контекста.
"""
def task_7():
    import json

    report = []
    with open('task_7.txt', 'r', encoding='UTF-8') as file:
        text = file.read()
        file.seek(0)
        profits = {}
        profit_sum = 0
        for row in file:
            items = row.split(' ')
            profit = int(items[2]) - int(items[3])
            if profit > 0:
                profits.update({items[0]: profit})
                profit_sum += profit
        report.append(profits)
        report.append({'average_profit': (profit_sum / len(profits))})

    with open('task07.json.tmp', 'w', encoding='UTF-8') as json_file:
        json.dump(report, json_file, ensure_ascii=False)

    json_report = json.dumps(report, ensure_ascii=False)

    print(f"Исходный файл:\n{text}\n")
    print(f"Список:\n{report}\n")
    print(f"json-объект:\n{json_report}")
if __name__ == "__main__":
    #task_1()
    #task_2()
    #task_3()
    #task_4()
    #task_5()
    #task_6()
    task_7()