a = int(input())
a1 = a // 100
a2 = (a//10)%10
a3 = a % 10
if a1==7 or a1==5 or a2==7 or a2==5 or a3==7 or a3==5:
    print("В записи числа есть 5 или 7")
else:
    print("В записи числа нет 5 или 7")
