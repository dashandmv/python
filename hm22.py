person = set(input())

all_digit = set('0123456789')
not_used_digit = list(all_digit - person)
if not_used_digit == []:
    print('число состоит из всех цифр')
else:
    not_used_digit.sort()
    print(not_used_digit)
    for i in not_used_digit:
        print(i, end = ' ')
