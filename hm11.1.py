x = int(input())
y = int(input())
next_day = 10/100
counter = 1
while x < y:
    x = x + (x * 10/100) 
    counter += 1
print(counter)
