list_name = ['Петя', 'Вася', 'Толя']
names = [(list_name[n], int(input())) for n in range(3)]

names.sort(key=lambda sub: sub[1], reverse=True)

print(names[0][0])
