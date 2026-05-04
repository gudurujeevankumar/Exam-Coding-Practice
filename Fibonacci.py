# N = int(input())
# a = 0
# b = 1

# for i in range(N):
#     print(a,end=" ")
#     a,b = b, a+b


n = int(input())

a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b