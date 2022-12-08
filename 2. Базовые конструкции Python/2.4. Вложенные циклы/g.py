n = int(input())
count = 1

for a in range(n):
    for b in range(3 + count, 1, -1):
        print(f'До старта {b - 1} секунд(ы)')

    print(f'Старт {count}!!!')

    count += 1
