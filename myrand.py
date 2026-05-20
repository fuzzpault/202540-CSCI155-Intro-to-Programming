#import random
import math as m
from random import *

print( m.sqrt(65))

for _ in range(100):
    r1 = randint(0,1000)
    #r2 = random.randint(0,1000)
    r2 = randint(0,1000)

    #print(f"r1: {r1:4}, r2: {r2:4}")
    print(f"{r1:4}\t{r2:4}\t{r1-r2}")