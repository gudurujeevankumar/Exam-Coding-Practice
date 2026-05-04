# TCS NQT Problem

n = int(input())
k = int(input())

happy = n
sad = 0

for _ in range(k):
    new_happy = (0.5 * sad + 0.3 * happy)
    new_sad = (0.7 * happy + 0.5 * sad)

    happy = int(new_happy)
    sad = int(new_sad)

print(happy)
print(sad)