# Specify the number of dashes. ------->

def arrow(length):
    for i in range(length):
        print('-', end="")
    print(">")

def darrow(length):
    print('<', end="")
    for i in range(length):
        print('-', end="")
    print(">")


def box(side):
    for _ in range(side):
        for _ in range(side * 2):
            print('X', end="")
        print()

def fancy_box(side = 5, inner_char = 'X'):
    # Top row
    print(f"+{'-' * (side - 2)}+")
    # Middle rows
    for _ in range(side - 2):
        print("|", end="")
        for _ in range(side - 2):
            print(inner_char, end="")
        print("|")
    # End row
    print(f"+{'-' * (side - 2)}+")



arrow(5)   # ----->
arrow(10)  # ---------->

darrow(50) # <----->

box(5) #.   xxxxx
       #.   xxxxx
       #    xxxxx
       #    xxxxx
       #    xxxxx

print()

fancy_box(5) #   +---+
            #.   |xxx|
            #    |xxx|
            #    |xxx|
            #    +---+

fancy_box(7, '.')

fancy_box()