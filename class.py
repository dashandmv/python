my_class = {
            'Masha' :
            {
                'rus' : [4, 5, 3, 4, 5],
                'math' : [3, 4, 4, 4, 4],
                'info' : [4, 5, 4, 5, 5, 5],
                'biology' : [3, 4],
                'chemistry' : []
            },
            'Misha' :
            {
                'rus' : [4, 5, 3, 4, 5],
                'math' : [4, 4],
                'info' : [5, 5, 5, 5],
                'biology' : [4, 5, 5],
                'chemistry' : []
            },
            'Gleb' :
            {
                'rus' : [5, 5, 5],
                'math' : [3, 4, 5, 4, 3, 4, 3, 4, 3],
                'info' : [4, 3, 4, 5, 3, 3],
                'biology' : [5, 5, 5, 5],
                'chemistry' : []
            },
            'Olya' :
            {
                'rus' : [],
                'math' : [],
                'info' : [],
                'biology' : [],
                'chemistry' : []
            }
            }


top = []
for i in range(len(my_class[list(my_class.keys())[0]])):
    top.append({})

my_class_keys = list(my_class.keys())

for i in my_class_keys:
    print(f'Student: {i}')
    subj = 0
    for j in list(my_class[i].keys()):
        if len(my_class[i][j]) > 0:
            mean_value = sum(my_class[i][j]) / len(my_class[i][j])
        else:
            meam_value = 0
        print(f'\tSubject: {j} -> {mean_value}')
        top[subj].update({i : mean_value})
        subj += 1
    print()

current_top = top
subj = 0
subj_names = list(my_class[list(my_class.keys())[0]].keys())

for i in current_top:
    print(subj_names[subj])
        
    min_value = 5
        
    min_name = ''
    for k in list(i.keys()):
        if i[k] <= min_value:
            min_value = i[k]
            min_name = k

    
    print(f'\t{min_name} -> {min_value}')
    subj += 1
    print()
