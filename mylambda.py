import random


def bad_add(a: int, b: int) -> int:
    # 90% of the time it is correct, otherwise off by 1
    if random.random() < 0.9:   # 90% of the time
        #print("correct")
        return a + b
    else:
        #rint("maybe this?")
        return "bob"
        return a + b + random.randrange(-1,1)

print( bad_add(1,2) + 100 )

what = lambda a,b: a + b

print( what(4,5))
