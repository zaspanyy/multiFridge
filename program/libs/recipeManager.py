
class RecipeAdder():
    
    def addIngredients(self):
        ingredients = input('input ingredient: ').lower()
        return ingredients
    
    def addQuantity(self):
        quantity = input('quantitty of an item: ')
        return quantity

    def addUnit(self):
        unit = input('units: ').lower()
        return unit
    
class RecipeDeleter():
    
    def deleteIngredient(self):
        ingredient = input('input ingredient to delete from recipe: ').lower()
        return ingredient