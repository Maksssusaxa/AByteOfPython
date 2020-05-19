def printMax(a, b):
    if a > b:
        print(a, 'Максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'Максимально')

printMax(3, 4) # Прямая передача значений

x = input('Введи число: ')
y = input('Введи число: ')

printMax(x, y)