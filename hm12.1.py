a = input()
index = -1
while index < len(a) -1:
    index += 1
    print(f"index = {index}")
    if a[index] == "a":
        continue
    if a[index] == "b":
        continue
    print(a[index])
