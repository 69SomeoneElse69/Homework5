# Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
control = 'start'
text_for_file = 'none'
my_file = open('Task1.txt', 'w', encoding='utf-8')
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
