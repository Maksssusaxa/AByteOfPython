number = 23
running = True

while running:
    guess = int(input('Введи целое число: '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False  # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
    # Здесь можно выполнить что-то еще

print('Завершение.')