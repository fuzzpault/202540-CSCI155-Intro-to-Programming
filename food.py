# Create 4 classes
# Donuts
#   Middle: cake, french, sour creme
#   Jelly Filled: Yes/No
#   Topping: Nothing, Chocolate, Glaze
# Pizza
#   Topping: pepperoni, cheese, veggies, pineapple, 
#   Sauce: BBQ, ranch, marinara, alfredo
#   Size: small, medium, large, sheet
# Bagels
#   Spreads: Cream Cheese, Butter, Jam
#   Middle: Plain, Everything, Onion, Cinimon Raisin 
#   Toasted: Yes/No
# Yogurt
#   Flavor: Plain, Strawberry, Mixed Berry, Coconut

# Food:
#   Calories: Float
#   Protein:
#   Serving Size:
#   Price: Float
#   --Sweet/Savory: Sweet, Savory, NA

class Food:
    def __init__(self, serving_size):
        self.serving_size = serving_size

    def info(self):
        print(f"  Calories: {self.getCalories()}")
        print(f"  Protein: {self.getProtein()}")

class Yogurt(Food):
    def __init__(self, serving_size, flavor):
        self.possibilities = ['Plain', 'Strawberry', 'Mixed Berry', 'Coconut']
        if flavor.title() not in self.possibilities:
            raise ValueError(f"{flavor} is not an option")
        self.flavor = flavor.title()    
        super().__init__(serving_size)

    def info(self):
        print(f"{self.flavor} Yogurt serving size: {self.serving_size} with this nutritional:")
        super().info()

    def getCalories(self):
        loc = self.possibilities.index(self.flavor)
        values = [60, 140, 145, 120]
        return values[loc] * self.serving_size # Calories
    
    def getProtein(self):
        return 6 * self.serving_size    # Grams

class Meal():
    def __init__(self):
        self.data = []

    def add(self, food):
        self.data.append(food)

    def __len__(self):
        ret = 0
        for food in self.data:
            ret += food.serving_size
        return ret
    
    def info(self):
        print(f"There are {len(self)} things in your meal")
        totCal = 0
        totProtein = 0
        for food in self.data:
            totCal += food.getCalories()
            totProtein += food.getProtein()
        print(f"  Calories: {totCal}")
        print(f"  Protein: {totProtein}")

meal = Meal()

meal.add( Yogurt(2, "mixed berry") )
meal.add( Yogurt(1, "plain"))

print(f"There are {len(meal)} things in your meal.")
meal.info()
