#number_grade = int(input("Enter your grade as a number: "))

for number_grade in range(105, -5, -1):
    print(f"{number_grade}: ", end="")
    if number_grade > 100:
        print("That's a grade above A!", end='')
    elif 90 <= number_grade:
        print('A', end='')
    elif 80 <= number_grade:
        print('B', end='')
    elif 70 <= number_grade:
        print('C', end='')
    elif 60 <= number_grade:   # Below 60 is an F.
        print('D', end='')
    elif 0 <= number_grade:
        print('F', end='')
    else:
        print("That's below 0.", end='')

    if 60 <= number_grade < 95:
        right_part = number_grade % 10
        #print(f"Right part {right_part}")
        if right_part >=6:
            print("+")
        elif right_part >= 3:
            print()
        else:
            print("-")

    if number_grade >= 95:  # Fix newline for grades >= 95
        print()

    if number_grade < 60:  # Fix newline for Fs
        print()
# Option #1 - Adjust ranges
# Option #2 - Take advantage of the pattern!
