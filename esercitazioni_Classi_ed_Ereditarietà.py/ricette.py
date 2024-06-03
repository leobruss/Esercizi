class RecipeManager:
    def __init__(self) -> None:
        self.ricettario = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> dict:
        if name not in self.ricettario:
            self.ricettario[name] = ingredients
            return {name : ingredients}
        else:
            raise ValueError("Ricetta già esistente")

    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict:
        if ingredient not in self.ricettario[recipe_name]:
            self.ricettario[recipe_name].append(ingredient)
            return {recipe_name : self.ricettario[recipe_name]}
        
        elif ingredient in self.ricettario[recipe_name]:
            raise ValueError("Ingrediente già esistente")
        
        elif recipe_name not in self.ricettario:
            raise ValueError("Ricetta non esistente")

    def remove_ingredient(self, recipe_name: str, ingredient: str) ->dict:
        if recipe_name in self.ricettario:
            if ingredient in self.ricettario[recipe_name]:
                self.ricettario[recipe_name].remove(ingredient)
                return {recipe_name: self.ricettario[recipe_name]}
            else:
                return "L'ingrediente non esiste"
        else:
            return "La ricetta non  esiste"
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) ->dict:
        if recipe_name in self.ricettario:
            ingredients = self.ricettario[recipe_name]
            if old_ingredient in ingredients:
                ingredients = [new_ingredient if ingredient == old_ingredient else ingredient for ingredient in ingredients]
                self.ricettario[recipe_name] = ingredients
                return {recipe_name: self.ricettario[recipe_name]}
            else:
                return "L'ingrediente non esiste"
        else:
            return "La ricetta non  esiste"
       

    def  list_recipes(self) -> None:
        return(list(self.ricettario.keys()))

    def list_ingredients(self, recipe_name: str) -> list:
        if recipe_name in self.ricettario:
            return(self.ricettario[recipe_name])
        elif recipe_name not in self.ricettario:
            raise ValueError("Ricetta non esistente")
        

    def search_recipe_by_ingredient(self, ingredient: str) ->list:
        ricette: dict = {}
        for recipe_name, ingredients in self.ricettario.items():
            if ingredient in ingredients:
                ricette[recipe_name] = ingredients
        if ricette:
            return ricette
        else:
            print("Nessuna ricetta ha questo ingrediente")


	
manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))

print("\n")
	
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

print("\n")

manager = RecipeManager()
print(manager.create_recipe("Spaghetti alla Carbonara", ["Spaghetti", "Uova", "Guanciale", "Pecorino Romano", "Pepe"]))
print(manager.search_recipe_by_ingredient("Uova"))