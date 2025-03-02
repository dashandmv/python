min_his = 1000000
words = ['lake' , 'fake' , 'summer' , 'pi' , 'rubber']
for i in words:
    if len(i) < min_his:
        min_his = len(i)
print(min_his)
