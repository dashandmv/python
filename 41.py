num = int(input())
n = int(input())
counter = 0
res = 0
while num > 0:
    v = num % 10
    res += v*n**counter
    counter += 1
    num = num // 10
print(res)
