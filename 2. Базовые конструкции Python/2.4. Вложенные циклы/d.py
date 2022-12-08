n = int(input())
c = [input() for _ in range(n)]
b = list(''.join(c))

print(sum([int(i) for i in b]))
