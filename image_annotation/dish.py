# This program have been created and tested with Python 3.5

class Ingredient:
    def __init__(self, name, nutritiveValue):
        self.name = name
        self.nutritiveValue = nutritiveValue
        # self.nutrientFactLabel = nutrientFactLabel
        # self.picturePath
    
    def __str__(self):
        return f"ingredient name -> {self.name}"


class Food:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.recipe = []
        
        # self.picturePath = ""
    
    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)
    
    def setIngredients (self, ingredients):
        self.ingredients = ingredients
    
    def getIngredients (self):
        return self.ingredients
    
    def setRecipe(self, recipe):
        self.recipe = recipe
    
    def getRecipe(self):
        return self.recipe
    
    def __str__(self):
        s = f"{self.name} :\n"
        for item in self.ingredients:
            s += f"---> {item}\n"
        
        return s
    

class Dish:
    def __init__(self, name, typeDish = "Main Course"):
        self.name = name
        self.foods = []
        self.condiments = []
        self.garnish = []
        
        self.typeDish = typeDish
        # self.categories = categories
        # self.picturePath = ""
    
    def addFood(self, food):
        self.foods.append(food)
    
    def setFoods(self, foods):
        self.foods = foods
    
    def getFoods(self):
        return self.foods
    
    def setCondiments(self, condiments):
        self.condiments = condiments
    
    def getCondiments(self):
        return self.condiments
    
    def setGarnish(self, garnish):
        self.garnish = garnish
    
    def getGarnish(self):
        return self.garnish
    
    def __str__(self):
        si = ""
        for item in self.foods:
            si += f"{item}\n"
        s = f"Dish '{self.name}' is of type {self.typeDish} with foods: \n{si}"
        return s


if __name__ == "__main__":
    bean = Ingredient("Arachide", "B")
    tomato = Ingredient("Tomato", "A")
    meat = Ingredient("Beef meat", "A")

    mealIngredients = []
    mealIngredients.append(bean)
    mealIngredients.append(tomato)
    mealIngredients.append(meat)

    foodBeanSauce = Food("Sauce d'Arachide")
    foodBeanSauce.setIngredients(mealIngredients)
    foodRice = Food("White Rice")
    foodRice.setIngredients([Ingredient("White Rice", "B"), Ingredient("Salt", "B")])

    dish = Dish("Riz Sauce Arachide")
    dish.setFoods([foodBeanSauce, foodRice])

    print(dish)