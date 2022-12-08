a = int(input())

for i in range(a):
    count = 1
    b = i + 1

    for n in range(1, a + 1):
        print(f'{n} * {b} = {n * b}')
