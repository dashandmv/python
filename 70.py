my_dict = {}
while 10>5:
    
    russian = input('Введите русское слово')
    if russian == '0':
        break
    english = input('Введите английсское слово')
    my_dict.update({russian: english})
    
print(my_dict)
