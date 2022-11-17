n = int(input())
temp = n
rev = 0

while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

print('YES' if temp == rev else 'NO')
