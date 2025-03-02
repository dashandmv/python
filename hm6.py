x = int(input())
if x == 0 and x <= 120:
    print("очень низкий рост")
elif x > 120 and x <= 140:
    print("низкий")
elif x > 140 and x <= 160:
    print("нормальный")
elif x > 160 and x <= 180:
    print("высокий")
elif x > 180:
    print("очень высокий")
else:
    print()
