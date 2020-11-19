# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
rus = []
dict_translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

my_file = open('Task4.txt', 'r', encoding='utf-8')
lenght_main = len(my_file.readlines())
my_file.seek(0)
eng_text = my_file.read()
print('исходный файл:', my_file.name, '\n', eng_text, '\n==============================')
my_file.seek(0)
rus_text = open('Task4_translate.txt', 'w+', encoding='utf-8')

for el in range(lenght_main):
    eng = my_file.readline()
    eng = eng.split(' ')
    name_translate = dict_translate[eng[0]]
    eng.insert(0, name_translate)
    eng.pop(1)
    rus_text.writelines(' '.join(eng))

rus_text.seek(0)
rus = rus_text.read()
print('переведенный файл:', rus_text.name, '\n', rus)
my_file.close()




rus_text.close()




