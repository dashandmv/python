x = int(input())  
p = int(input())  
y = int(input())  
counter = 0
while x < y:
    x = x + (p/100)*x
    counter += 1
print(counter)
