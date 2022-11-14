import itertools

a = list(map(int, input()))
b = list(map(int, input()))

if len(a) > len(b):
    b.insert(0, 0)

result = [x + y for x, y in itertools.zip_longest(a, b, fillvalue=0)]

arr = []

for n in result:
    arr.append(str(n)[-1:])

print(''.join(arr))
