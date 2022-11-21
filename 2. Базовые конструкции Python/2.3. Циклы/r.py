n = int(input())
c = 2
a = []

while n > 1:
    if n % c == 0:
        a.append(c)
        n /= c
    else:
        c += 1

print(*a, sep=' * ')
