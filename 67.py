my_set = set()

steps = int(input())
for i in range(steps):
    comand = input()
    signt = comand[0]
    num = int(comand[2:len(comand)])
    if signt == '+':
        my_set.add(num)
    else:
        my_set.discard(num)

new = list(my_set)
new.sort()
print(new)
    
    
