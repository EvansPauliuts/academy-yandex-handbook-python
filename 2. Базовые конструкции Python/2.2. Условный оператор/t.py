a = [input() for _ in range(3)]

b = [n for n in a if 'зайка' in n]
s = min(b)

print(''.join(s), len(''.join(s)))
