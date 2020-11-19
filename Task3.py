# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
aver = 0
my_file = open('Task2.txt', 'r', encoding='utf-8')
lenght_main = len(my_file.readlines())
my_file.seek(0)
for el in range(lenght_main):
    numbers = my_file.readline()
    numbers = numbers.split(' ')
    name = numbers.pop(0)
    numbers = [int(x) for x in numbers]
    aver = aver + sum(numbers)
    if sum(numbers) < 20000:
        print(name, sum(numbers), "<= Solary < 20.000")
    else:
        print(name, sum(numbers))


my_file.close()

print("\nна", lenght_main ,"сотрудников\nсредняя з.п.: ", aver / lenght_main)
