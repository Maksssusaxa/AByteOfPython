while True:
    s = input('Введите что нибудь: ')
    if s == 'выход':
        print('Завершение...')
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введенная строка достаточной длины')
    # Разные другие действие здесь