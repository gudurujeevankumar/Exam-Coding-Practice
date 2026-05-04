n = int(input())
count = 0

while n > 0:
    last = n % 10
    count += 1
    n //= 10
print(count)

# if n < 0 :
#     n *= -1

# print(len(str(n)))