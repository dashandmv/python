import random 
print("эта игра загадывает рандомное число, которое нужно угадать с трех попыток")

secret = random.randint(1,10)
#print(secret)
counter = 0
while counter < 3:
    counter += 1
    a = int(input())
    if a > secret:
        print("загаданное число меньше")
    elif a < secret:
        print("загаданное число больше")
    else:
        print("вы угадали")
        break
    

else:
    print(f"вы проиграли, число {secret}")
