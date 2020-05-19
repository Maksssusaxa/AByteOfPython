poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python!
'''

f = open('poem.txt', 'w') # Открываем для записи (writing)
f.write(poem)
f.close()

f = open('poem.txt') # Если не указан режим, по умолчанию стоит 'reading'

while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длинна обозначает конец файла (EOF)
        break
    print(line, end=" ")

f.close()