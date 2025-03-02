my_dict = {}
while 10>5:
    slovo = input('Введи слово: ')
    if slovo == '0':
        break
    sinonim = input('Введи синоним: ')
    my_dict.update({slovo: sinonim})
print(my_dict)

person = input()
k = list(my_dict.keys())
for i in k:
    if person == i:
        print(my_dict[i])
        break
    elif person == my_dict[i]:
        print(i)
        break

else:
    print('слова нет')
