numbers = [1, 3, 3, 6, 7, 4, 4, 5, 10]
a = list(set(numbers))
counter = 0
for i in a:
    counter += i
print(counter)
