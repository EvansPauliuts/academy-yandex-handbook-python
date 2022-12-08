n = int(input())
count = 0

for num in range(n):
    number = int(input())

    if number <= 1:
        continue

    flag = True
    k = number - 1

    while k > 1:
        if number % k == 0:
            flag = False
            break
        k -= 1

    if flag:
        count += 1


print(count)
