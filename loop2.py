
a = ['bob','mary', 123, 'pizza']
# Assign i in each loop to each element in a.
for i in a:
    print(i)

print()

#for i in 
print( a[0] )
print( a[1] )
# ....
#print( a[7])

print()

# Index-like method
for i in range(len(a)):
    print(f"{i}: {a[i]}")

print()

# Enumerate way
print("Enumerate")
for (i,value) in enumerate(a):
    print(i, value)

print()

b = {5:1, 8:2, 10:3}
for i in b:
    print(i)

print()
# Not that useful
for i in enumerate(b):
    print(i)

for (k,v) in b.items():
    print(k,v)

print()

for k in b.keys():
    print(k, b[k])

print()

c = (1,5,3,4,7)
for i in c:
    print(i)

d = set()
d.add(1)
d.add(6)
d.add('hi')

print()

for i in d:
    print(i)