a = ['pasta', 'sushi', 'steak', 'pasta2', "Rice", 'hot dogs', "Rice", "Jallof Rice"]

print(a)
a.sort()
print(a)

a.append(12)
a.append(6.9)

print(a)
print(len(a))
print(f"pop: {a.pop()}")

print(a)

print(len("This is a string"))

a.remove("Rice")

print(a)
loc = a.index("steakk")
print(loc)
print(a[loc])
