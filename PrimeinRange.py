start = int(input())
end = int(input())

for n in range(start,end+1):
    if n < 2:
        continue
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        print(n,end = " ")