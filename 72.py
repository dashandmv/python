
# age = int(input("Сколько тебе лет?: "))
# print("Ваш возраст: " + str(age))

# numbers = [1, 2, 3, 4, 5]
# count = 0
# for i in numbers:
#     count += i
# middle = count / len(numbers)
# print("Среднее значение: " + str(middle))
try:
    num = 50
    person = int(input())
    if person > 50:
        print("Число больше 50")
    else:
        print("Число меньше 50")
except ValueError:
    print("Ошибка")
