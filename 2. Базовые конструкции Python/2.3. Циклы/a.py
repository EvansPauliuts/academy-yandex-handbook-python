count = 0

while True:
    input_name = input().lower()

    if input_name == 'три!':
        for _ in range(count):
            print('Режим ожидания...')

        print('Ёлочка, гори!')
        break
    else:
        count += 1
