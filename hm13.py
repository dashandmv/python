num = int(input())
counter = 0
while num > 0:
    last_num = num % 10
    counter += 1
    num = num // 10
print(f"counter = {counter}")
