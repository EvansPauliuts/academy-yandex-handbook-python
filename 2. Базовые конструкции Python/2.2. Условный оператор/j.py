num = input()

num_small = int(num[0]) + int(num[1])
num_big = int(num[1]) + int(num[-1])

result = [num_small, num_big]
result.sort(reverse=True)
print(int(''.join([str(i) for i in result])))
