s = input()
print(s[::-1])

n = int(input())
rev = 0

while n > 0:
    last = n % 10
    rev = rev * 10 + last
    n //= 10
print(rev)