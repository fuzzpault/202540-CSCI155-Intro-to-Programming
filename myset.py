pasta1 = set()
pasta2 = set( [1,2,3, 6, 3, 4, 10, 34, 11] )

print(pasta1)
print(pasta2)
pasta2.add(88)
pasta2.remove(2)

print(len(pasta2))

if 10 in pasta2:
    print("10 is in the set")
else:
    print("10 is NOT in the set")

a = ['pasta', 'sushi', 'steak', 'pasta', "Rice", 'hot dogs', "Rice", "Jallof Rice"]

a = list(set(a))
print(a)