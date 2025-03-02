num = int(input())
summ = 0
while num > 0:
    last_num = num % 10
    summ = summ + last_num
    num = num // 10
print(summ)
