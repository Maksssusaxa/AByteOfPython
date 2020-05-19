name = 'Swaroop'

if name.startswith('Swa'):
    print('Начинается на Swa')

if 'a' in name:
    print('Содержит строку "a"')

if name.find('war') != -1:
    print('Содержит строку "war"')

delimiter = '_*_'

mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))

