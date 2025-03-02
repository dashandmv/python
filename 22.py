a = input()
if len(a)%2 != 0:
    print(a[len(a)//2])
else:
    print(a[len(a)//2 - 1])
    print(a[len(a)//2])
