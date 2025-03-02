my_dict = {'Ann': 80, 'Nikolay': 40, 'Sofiya': 55, 'lena': 35, 'Petr': 90, 'Misha': 60}

k = list(my_dict.keys())
person = int(input())
for i in k:  
    if my_dict[i] < person:
        del my_dict[i]
print(my_dict)

