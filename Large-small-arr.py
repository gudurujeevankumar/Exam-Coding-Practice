my_set = set(map(int,input().split(',')))
l = list(my_set)
s = sorted(l)

print("sorted :",s)
print("Heighest :",s[-1])
print("Second Heighest :",s[-2])
print("Lowest :",s[0])