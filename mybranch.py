# Branching or conditionals
import random

counts = {'icecream':0, 'chicken':0, 'rice':0}
#
icecream_counts = 0
chicken_counts = 0
#....

counts2 = [0,0,0]


for _ in range(10000):
    if random.randint(0,100) > 50:
        #print("You get icecream")
        counts['icecream'] += 1.  # counts['icecream'] = counts['icecream'] + 1
        counts2[0] += 1
    elif random.randint(0,100) > 50:
        #print("Chicken tenders")
        counts['chicken'] += 1
    else:
        #print("Rice")
        counts['rice'] += 1


print(counts)

# if - can stand alone
# elif - else if
# else