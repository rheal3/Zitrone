import os
import json

# Main Entry Function
def main():
    os.system('clear')
    print("""Welcome to Zitrone!
    This is an app that allows you to create recipes and store them in your own personal database.
    Let's get started!
    To begin you're going to need to know a few simple commands:
        {0}exit{1}: exit the program
        {0}input{1}: input a new recipe
        {0}database{1}: view a list of all of your inputted recipes
        {0}help{1}: view this list of the commands""".format('\033[1m', '\033[0m'))
    return input("What would you like to do (input/database/help/exit)? ")


# Input Recipe Functions
def gather_ingredients():
    ingredients = {}
    ingredient = ""
    while ingredient.lower().strip() != "done":
        ingredient = input("Ingredient: ")
        if ingredient == "done":
            return ingredients
        elif ingredient == '':
            continue
        amount = input(f"Amount of {ingredient}: ").strip()
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
        recipe_by_ingredients[ingredient] = [recipe_name]
    return recipe_by_ingredients



# Search Functions
def append_record(dictionary):
    with open('ingredient_search', 'a') as file:
        json.dump(dictionary, file)
        file.write(os.linesep)

def access_record():
    ingredients_dictionary = {}
    with open('ingredient_search') as file:
        record_list = [json.loads(line) for line in file]
        for line in record_list:
            for key, value in line.items():
                if key not in ingredients_dictionary:
                    ingredients_dictionary[key] = value
                else:
                    ingredients_dictionary[key] += value
    return ingredients_dictionary

def search_by_ingredient(ingredient_to_find, ingredient_search):
    recipes_with_ingredient = []
    for ingredient in ingredient_search:
        if ingredient == ingredient_to_find:
            recipes_with_ingredient += ingredient_search[ingredient]
    return recipes_with_ingredient

def sort_recipes_by_most_ingredients(recipes_mult_ingredients):
    highest_value_recipe = ""
    highest_value = 0
    for recipe, amount in recipes_mult_ingredients.items():
        if amount > highest_value:
            highest_value_recipe = recipe
    return highest_value_recipe



# Database Functions
def list_of_recipes(database_list):
    for i in range(0, len(database_list)):
        database_list[i] = database_list[i].replace("./recipe_database/", "").replace(".txt", "").lower()
        print(database_list[i].title())
    print("\n", end="")


def open_recipe(database_list):
    recipe_to_access = input("Which recipe would you like to view? ")
    while recipe_to_access.lower().strip() not in database_list:
        print("Recipe not in database.")
        recipe_to_access = input("Which recipe would you like to view? ")

    if recipe_to_access in database_list:
        os.system('clear')
        file_to_open = open(os.path.join('./recipe_database/', database_list[database_list.index(recipe_to_access)] + '.txt'), 'r')
        for line in file_to_open:
            print(line, end="")
        print("\n")
    return input("Would you like to access another recipe? (y/n) ").lower().strip()


# Help Functions
def help():
    print("I see you've found the tremendously helpful help page!")
    print("""List of Commands:
        {0}exit{1}: exit the program
        {0}input{1}: input a new recipe
        {0}database{1}: view a list of all of your inputted recipes
        {0}help{1}: view this list of the commands""".format('\033[1m', '\033[0m'))
    # print("""About Zitrone:
    # Zitrone allows you to input your recipes and store them to a database.""")
