arr = list(map(int, input().split(',')))

first = second = float('-inf')
lowest = float('inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
    if num < lowest:
        lowest = num

print("Highest:", first)
print("Second Highest:", second)
print("Lowest:", lowest)