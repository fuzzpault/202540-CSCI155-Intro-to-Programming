 
a = 5
b = 10

def add(first,second):
    global a
    first = first + 1
    a = 22
    print(f"inside a: {a}")
    return first + second

print(add(a,b))

print(f"a: {a}")
print(f"b: {b}")

c = [1,2,3]

def print_list(mylist):
    mystery = 234234
    mylist.append(89)
    print(locals())
    print(f"Inside: {mylist}")

print_list(c)
print(f"Outside: {c}")
print(__file__)
print(globals())