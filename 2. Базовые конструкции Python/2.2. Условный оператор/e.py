n, m = [int(input()) for _ in range(2)]

names_and_apple_num = [
    ('Петя', 4 + n),
    ('Вася', 9 + m),
    ('Толя', 0),
    ('Геня', 2),
    ('Дима', 0)
]

names_and_apple_num.sort(key=lambda sub: sub[1], reverse=True)

print(names_and_apple_num[0][0])
