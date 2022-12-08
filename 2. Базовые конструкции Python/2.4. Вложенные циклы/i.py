n = int(input())
num_val = [list(input()) for _ in range(n)]
find_max_num = [max(i) for i in num_val]

print(''.join(find_max_num))
