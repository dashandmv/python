string = "ayueohgfue"
current_len = 1
max_len = 0


for i in range(0 , len(string)- 1):
    if string[i] in "eyuioa" and string[i + 1] in "eyuioa":
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 1
if current_len > max_len:
    max_len = current_len

print(max_len)


#for i in string:
 #   if i in "eyuioa":
  #      counter += 1
