import math

a, b = [int(input()) for _ in range(2)]
print((a * b) // math.gcd(a, b))
