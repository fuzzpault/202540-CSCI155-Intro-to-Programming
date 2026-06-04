class CandSDog: 
    count = 0.  # Static member variable - shared between ALL instances.
    def __init__(self, age, name, breed, color, gender):
        self.age = age
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender   
        print()
        CandSDog.count += 1
         
    
    def __str__(self):
        return f"{self.name} is a {self.color} {self.breed} who is {self.age} years old."
    
    def bark(self):
        print(f"{self.name} just barked.")

dog_list = []

if False:
    for _ in range(4):
        age = int(input("what is dog age: "))   
        name = input("What is the dog's name?: ") 
        breed = input("What's the dog's breed?: ")
        color = input("what is the dogs color?: ")
        gender = input("what is the dogs gender?: ")
        dog_list.append(CandSDog(age, name, breed, color, gender))

dog_list.append( CandSDog(14, "Archie", "Good","Brown", "Male") )
dog_list.append( CandSDog(16, "Sarah", "Bichan","White", "Female") )
dog_list.append( CandSDog(6, "Bear", "Yorkie","Black", "Male") )

print(CandSDog.count)


for d in dog_list:
    print(d)
    d.bark()