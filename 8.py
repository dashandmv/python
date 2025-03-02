a = int(input())
a1 = a // 10
a2 = a % 10
if a1 > a2:
    print("first")
elif a2 > a1:
    print("second")
else:
    print("equal")
