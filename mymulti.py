a = {}
a['csci155-summer'] = ['Brooklyn', 'Queena', 'Connor'] 
a['csci155-fall'] = []

# a is a dictionary with strings as keys and lists as values.  
# Each list contains strings.
print(a)

# Difference between a list and a set
#   List can have duplicates
#   Lists have order!  sets don't.
#   What operation on a set is faster than that on a list? Searching and adding

# What is the difference between a list and a tuple?
#   Create a list with [], tupple uses ()
#   Tuple are not mutable
b = (1,5,3,7,8,'yi','billy')
b[3] = 900
print(b)