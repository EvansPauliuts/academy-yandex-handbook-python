list_name = ['Петя', 'Вася', 'Толя']
names = [(list_name[n], int(input())) for n in range(3)]


names.sort(key=lambda sub: sub[1], reverse=True)

for i, n in enumerate(names, start=1):
    print(f'{i}. {n[0]}')
