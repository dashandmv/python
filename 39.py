counter = 0
while counter < 20:
    counter += 1
    if counter % 3 != 0:
        continue
    print(f"counter = {counter}")
