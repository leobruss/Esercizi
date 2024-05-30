class Animal:
    def __init__(self, name: str, legs:int) ->None:
        self.name = name
        self.legs = legs
    def get_legs(self) -> None:
        return self.legs 
    
    def set_legs(self, legs: str) ->str:
        self.legs = legs

    def print_info(self) ->None:
        print(f"The animal {self.name} has {self.legs}")

animal1: Animal = Animal("Lion", 4)
animal2: Animal = Animal("Fish", 0)
print(animal1.name)
print(animal2.name)
animal1.legs = 4
animal2.set_legs(0)
animal1.print_info()
animal2.print_info()
print("\n")

from typing import List

class Food:
    def __init__(self, name: str, price: str, description: str) -> None:
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self, foods=None):
        if foods is None:
            self.foods: List[Food] = []
        else:
            self.foods: List[Food] = foods
    
    def addFood(self, food):
        self.foods.append(food)
    
    def removeFood(self, food):
        self.foods.remove(food)
    
    def printPrices(self):
        print("Menu:")
        for food in self.foods:
            print(f"{food.name}: ${food.price}")
    
    def getAveragePrice(self):
        if not self.foods:
            return 0
        total_price = sum(food.price for food in self.foods)
        return total_price / len(self.foods)

food1 = Food("Pizza", 10, "Delicious Italian pizza")
food2 = Food("Burger", 8, "Classic beef burger")
food3 = Food("Sushi", 15, "Japanese sushi rolls")

menu = Menu()
menu.addFood(food1)
menu.addFood(food2)
menu.addFood(food3)     

food4 = Food("Pasta", 12, "Homemade spaghetti")
food5 = Food("Salad", 7, "Fresh garden salad")

menu.addFood(food4)
menu.addFood(food5)

menu.printPrices()

average_price = menu.getAveragePrice()
print("Average price of the menu:", average_price)