# Key:value pairs
# Map
a = {'steak': 5.6, 'rice': 3.4, 'icecream': 3.0, }
a= {}
import pprint

print(a)
print(a['rice'])
a['icecream'] = 'chocolate'

print(a)

print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))

b = list(a.items())

print(b[0])

print(b[-1][-1])

c = [b, a]

print(c)
pprint.pprint(c)
