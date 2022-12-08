a = int(input())
new_list = []
count = 1
st = 0

for i in range(a):
    new_list.append([])
    c = (i + 1) + i

    for n in range(count):
        st += 1

        new_list[i].append(str(st))

        if st == a:
            break

    if st == a:
        break

    count += 1


for i in new_list:
    print(' '.join(i))
