#  TCS 1st April shift 1 question 1
# Laptops eligibilty more than or equal to capacity 


n = int(input())
l = list(map(int,input().split()))
c = int(input())
count = 0

for lap in l:
    if lap >= c:
        count += 1

print(count)
