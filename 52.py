a = input()
colors = ['blue' , 'green' , 'purpule' , 'yellow']
for i in colors:
    if i == a:
        print(f'нашелся цвет {a}')
        break
else:
    print(f'не нашелся цвет {a}')
