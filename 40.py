a = input()
index = -1
while index < len(a) -1:
    index += 1
    print(f"index = {index}")
    if a[index] == a[index].lower():
        continue
    print(a[index])
        
