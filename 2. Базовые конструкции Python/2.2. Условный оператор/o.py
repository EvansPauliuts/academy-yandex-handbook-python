a, b = [input() for _ in range(2)]
x = [*list(a), *list(b)]
m = x.pop(x.index(max(x)))
n = x.pop(x.index(min(x)))
s = sum([int(i) for i in x])

print(f'{m}{str(s)[-1]}{n}')
