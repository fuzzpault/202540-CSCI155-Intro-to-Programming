a = [5,6,8,3,2]

a.append(100)

print(a)
print(a[0])
print(a[1])
print(a[2])

print(a[-1])
print(a[-2])

# List slicing - gives a new list!
print(a[:-1])
print(a[2:])

print(a[:])

a[-1] = 67
print(a)