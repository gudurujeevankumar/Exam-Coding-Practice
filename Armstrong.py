n = int(input())
temp = n
digits = len(str(n))
total = 0

while temp > 0:
    last = temp % 10
    total += last ** digits
    temp //= 10

print(total == n)