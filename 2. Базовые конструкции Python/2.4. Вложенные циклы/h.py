n = int(input())
name_mount = []

for _ in range(n):
    input_name = input()
    input_num = input()

    name_mount.append(tuple((input_name, sum(list([int(i) for i in input_num])))))

name_mount.reverse()
max_tuple = max(name_mount, key=lambda x: x[1])
print(max_tuple[0])
