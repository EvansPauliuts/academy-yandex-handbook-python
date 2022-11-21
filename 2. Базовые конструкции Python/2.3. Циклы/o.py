n = int(input())
count = 0

for i in range(n):
    input_value = input()

    if 'зайка' in input_value:
        count += 1

print(str(count))
