# Make a Dog class that stores their age, name, breed, color, gender
# Create a new python file first-first.py and create that class in it.
# Then create 4 dogs and put them all in a list.


class Car:
    # year, make, model, color
    def __init__(self, year, make, model, color):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        print("INIT called")

    def __str__(self):
        return f"Car instance Year: {self.year}\tMake: {self.make}\tModel:{self.model}\tColor:{self.color}"

    def myprint(self):
        print(f"Car instance Year: {self.year}\tMake: {self.make}\tModel:{self.model}\tColor:{self.color}")

    def __eq__(self, other):
        #print(f"This: {self}")
        #print(f"Other: {other}")
        return self.year == other.year
    
    def getYear(self):  # Getter function - allows someone outside the class to get information about 
        #   the instance
        return self.year
    
    def setYear(self, new_year):
        self.year = new_year


if __name__ == "__main__":
    mylist = []

    mylist.append( Car(2011, "Dodge", "Durango", "Silver") )
    mylist.append( Car(1970, "Chevy", "SuperSport", "Red") )
    mylist.append( Car(2018, "Kia", "Stinger", "Blue") )
    mylist.append( Car(2018, "Toyota", "Sienna", "Black") )

    if mylist[2] == mylist[3]:
        print("They are the same")

    for i in mylist:
        print(i)
        i.myprint()

    mylist[-1].setYear(1999)
    for i in mylist:
        print(i)