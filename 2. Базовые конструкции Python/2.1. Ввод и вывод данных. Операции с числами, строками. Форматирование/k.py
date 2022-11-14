n = input()
num_arr = [n[a] for a in range(len(n))]

new_arr = list(reversed(num_arr[:2])) + list(reversed(num_arr[2:]))
print(''.join(new_arr))
