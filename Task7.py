# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import  json
firm_dict = {}
average_profit = 0
average_profit_dict = {}
my_file = open('Task7.txt', 'r', encoding='utf-8')
lenght_main = len(my_file.readlines())
my_file.seek(0)

for el in range(lenght_main):
    line = my_file.readline()
    line = line.split(' ')
    name = line[0]
    balance = int(line[2]) - int(line[3])
    if balance > 0:
        average_profit = average_profit + balance
    else:
        print(name, 'не участвует в расчете среднего дохода')

    firm_dict[name] = balance
my_file.close()
average_profit_dict['average_profit'] = average_profit / lenght_main
string_for_json = [firm_dict, average_profit_dict]
print(string_for_json)

with open("Task7_json.json", "w") as json_file:
    json.dump(string_for_json, json_file)
