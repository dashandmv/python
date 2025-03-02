person = int(input('Введите количество шагов: '))

my_set = set()
for i in range(0, person):
    step = int(input())
    if step in my_set:
        print('yes')

        
    else:
        print('no')
        my_set.add(step)
    
    
