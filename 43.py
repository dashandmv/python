a = int(input())
counter = 0
while True:
    if a == 0:
        break
    if a%5 == 0:
        counter += 1

    a = int(input())
print(f"counter = {counter}")
    
    
