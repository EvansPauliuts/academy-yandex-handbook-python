n = int(input())
list_num = list(str(n))

new_list = [int(n) for n in list_num if int(n) % 2 == 1]
print(*new_list, sep='')
