a = input()
index = -1
counter = 0
while index < len(a) -1:
    index +=1
    
    if a[index] == "a":
        counter += 1
    elif a[index] == "e":
        counter += 1
    elif a[index] == "i":
        counter += 1
    elif a[index] == "o":
        counter += 1
    elif a[index] == "u":
        counter += 1
    elif a[index] == "y":
        counter += 1
print(f"counter = {counter}")
    
    
