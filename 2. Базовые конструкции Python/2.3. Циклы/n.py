input_num = int(input())

if input_num > 1:
    for i in range(2, int(input_num / 2) + 1):
        if (input_num % i) == 0:
            print('NO')
            break
    else:
        print('YES')

else:
    print('NO')
