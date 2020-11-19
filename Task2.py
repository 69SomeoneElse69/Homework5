# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# я использую файл созданный ранее в задании Task1
my_file = open('Task1.txt', 'r', encoding='utf-8')

lines = my_file.read().splitlines()
my_file.close()

# содержимое файла
print(my_file.name, lines)

# выполнить подсчет количества строк,
print('количество строк:', len(lines))

# количества слов в каждой строке.
num_words = [('количество слов в "' + sentence + '": ' + str(len(sentence.split()))) for sentence in lines]
print('\n'.join(map(str, num_words)))
