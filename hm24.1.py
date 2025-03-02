food = {'apple': 10, 'banana': 20, 'cherries': 30}
v = list(food.values())
max_prise = 0
for i in v:
    if i > max_prise:
        max_prise = i
    
print(max_prise)


    
