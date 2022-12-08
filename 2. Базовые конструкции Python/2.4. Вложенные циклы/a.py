a = int(input())
list_new = []


for i in range(a):
    count = 0
    b = i + 1
    list_new.append([])
    for n in range(1, a + 1):
        list_new[i].append(str(n * b))

    count += 1


for i in list_new:
    print(' '.join(i), sep=' ')
