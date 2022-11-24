M, N, K1, K2 = [
    int(input()) for _ in range(4)
]

X = M * (K2 - N) / (K2 - K1)
Y = M - X
print(int(X), int(Y), sep=' ')
