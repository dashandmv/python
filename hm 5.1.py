a = int(input())
a1 = a // 1000
a2 = (a // 100)%10
a3 = (a // 10) % 10
a4 = a % 10

counter = 0

if a1%2 != 0:
    counter += 1
if a2%2 != 0:
    counter += 1
if a3%2 != 0:
    counter += 1
if a4%2 != 0:
    counter += 1

print(counter)
