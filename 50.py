string = "AaaaBcAaaBCB"
current_len = 1
max_len = 0

for i in range(0 , len(string)):
    if string[i] == string[i].lower() and string[i + 1] == string[i + 1].lower():
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 1

if current_len > max_len:
    max_len = current_len

print(max_len)
