import os

# Main Entry Function
def main():
    os.system('clear')
    print("""Welcome to {}!
    This is an app that allows you to create recipes and store them in your own personal database.
    Let's get started!
    To begin you're going to need to know a few simple commands:
    To input a new recipe you will use the 'input' command.
    If you want to view your database of recipes you can do so by typing 'database' command.
    If you ever need help, you can type in the 'help' command.
    To exit the program type 'exit'.""")
    return input("What would you like to do (input/database/exit)? ")


# Input Recipe Functions
def gather_ingredients():
    ingredients = {}
    ingredient = ""
    while ingredient != "done":
        ingredient = input("Ingredient: ")
        if ingredient == "done":
            return ingredients
        elif ingredient == '':
            continue
        amount = input(f"Amount of {ingredient}: ")
        ingredients[ingredient] = amount
    return ingredients

def gather_recipe_steps():
    count = 1
    method = {}
    step = ""
    while step != "done":
        step = input(f"Step {count}: ")
        if step == "done":
            return method
        method[count] = step
        count += 1

def format_recipe(recipe_name, recipe_ingredients, recipe_steps):
    completed = f"""\n{recipe_name.title()}
    \nIngredients: """
    for ingredient, amount in recipe_ingredients.items():
        completed += f"\n{amount:<8} {ingredient.lower()}"
    completed += "\n\nSteps: "
    for count, step in recipe_steps.items():
        completed += f"\nStep {count}:  {step}"
    return completed

def save_recipe(recipe_name, compiled_recipe):
    text_file = open(f"{recipe_name}.txt", "w")
    text_file.write(compiled_recipe)
    text_file.close()

def store_recipe_by_ingredients(ingredients_dictionary, recipe_name):
    recipe_by_ingredients = {}
    for ingredient, amount in ingredients_dictionary.items():
        recipe_by_ingredients[ingredient] = recipe_name
    return recipe_by_ingredients



# Database Functions
def list_of_recipes(database_list):
    for i in range(0, len(database_list)):
        database_list[i] = database_list[i].replace("./recipe_database/", "").replace(".txt", "").lower()
        print(database_list[i].title())
    print("\n", end="")


def open_recipe(database_list):
    recipe_to_access = input("Which recipe would you like to access? ")
    while recipe_to_access.lower() not in database_list:
        print("Recipe not in database.")
        recipe_to_access = input("Which recipe would you like to access? ")

    if recipe_to_access.lower() in database_list:
        os.system('clear')
        file_to_open = open(os.path.join('./recipe_database/', database_list[database_list.index(recipe_to_access)] + '.txt'), 'r')
        for line in file_to_open:
            print(line, end="")
        print("\n")
    return input("Would you like to access another recipe? (y/n) ")


# Help Functions

def help():
    'exit'
    'input'
    'database'
