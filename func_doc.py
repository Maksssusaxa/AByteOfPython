def printMax(x,y):
    '''Выводит максимально из двух чисел.

        Оба числа должны быть целыми числами.'''
    x = int(x) # Конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'Наибольшее')
    else:
        print(y, 'Нибольшее')

printMax(3, 5)
print(printMax.__doc__)