# Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
import re

control = 'start'
text_for_file = 'none'
my_file = open('Task5.txt', 'w', encoding='utf-8')
while text_for_file != '':
    text_for_file = str(input('Введите следующую строку: '))
    if text_for_file == '':
        break
    if control == 'second':
        my_file.write('\n' + text_for_file)
    else:
        my_file.write(text_for_file)
        control = 'second'
my_file.close()
print('Введенные данные были сохранены в файл:', my_file.name)

# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
my_file = open('Task5.txt', 'r', encoding='utf-8')
my_sum = 0
numbers = my_file.read()
print('читаем файл:\n', numbers)
numbers = re.findall(r'[+-]?\d+', numbers) # находим все числа без/с префиксами + и -
print('Общая сумма чисел в файле "' + str(my_file.name) + '":', sum([int(x) for x in numbers]))
