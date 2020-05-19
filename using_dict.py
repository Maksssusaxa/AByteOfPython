ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
     }

print("Адрес Swaroop'a:", ab['Swaroop'])

del ab['Spammer']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, adress in ab.items():
    print('Контакс {0} с адресом {1}'.format(name, adress))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдресс Guido:", ab['Guido'])
