my_dict = {'Sasha':4, 'vera':5, 'lera':3}
k = list(my_dict.keys())
person = int(input())
for i in k:
    if my_dict[i] >=person:
        print(i)
    
