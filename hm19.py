counter = 0

person = list(map(int, input("Введите список чисел через пробел: ").split()))
print(f"Исходный список: {person}")
n = len(person)

for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if person[j] > person[j+1]:
            person[j], person[j+1] = person[j+1], person[j]
            swapped = True
            counter += 1
    if not swapped:
        break

print(f"Отсортированный список: {person}")
print(f"Количество произведенных замен: {counter}")
