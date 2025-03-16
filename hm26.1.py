try:
    person = int(input('Введите свою оценку от 0 до 100: '))
    if person > 0 and person < 30:
        print('Ты можешь лучше!')
    elif person < 50:
        print('Удовлетворительно!')
    elif person < 70:
        print('Хорошая работа!')
    elif person < 90:
        print('Отличная работа!')
    else:
        print('Замечательная работа!')
except ValueError:
    print('Ошибка')