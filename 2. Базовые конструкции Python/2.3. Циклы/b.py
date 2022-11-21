count = 0

while True:
    input_value = input().lower()

    if input_value == 'приехали!':
        break
    else:
        if 'зайка' in input_value:
            count += 1

print(str(count))
