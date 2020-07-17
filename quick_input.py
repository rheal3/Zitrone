import input_functions
import search_functions
import os

def quick_input():
    os.system('clear')

    print("I see you've decided to input a recipe!")
    recipe_name = input("What is the name of the recipe? ").title().strip()
    potential_path = f'./recipe_database/{recipe_name.lower()}.txt'

    if os.path.exists(potential_path):
        print(f"There is already a recipe called {recipe_name} in your database.")
        recipe_name = input("What would you like to name the recipe? ").title().strip()

    os.system('clear')

    print("Sounds delicious!")
    print("Now let's enter some ingredients. We'll enter the ingredients first and then the amount that we need after.")
    print("When you finish type {0}'done'{1} to move to the next step.".format('\033[1m', '\033[0m'))

    ingredients = input_functions.gather_ingredients()

    os.system('clear')

    print("Now that we've entered the ingredients, let's type in the method.")
    print("Once again you can type in {0}'done'{1} when you are finished.".format('\033[1m', '\033[0m'))

    recipe_steps = input_functions.gather_recipe_steps()

    os.system('clear')

    print("Compiling recipe . . .")

    compiled_recipe = input_functions.format_recipe(recipe_name, ingredients, recipe_steps)

    print(compiled_recipe)

    save = input("\nWould you like to save the recipe to your database? (y/n) ").lower().strip()
    while save != 'y' and save != 'n':
        print("Command not understood.")
        save = input("Enter a valid command. (y/n) ").lower().strip()

    if save == 'y':
        if not os.path.exists('./recipe_database'):
            os.makedirs('./recipe_database')
        input_functions.save_recipe(os.path.join('./recipe_database', recipe_name.lower()), compiled_recipe)

        recipe_by_ingredients = {}
        recipe_by_ingredients.update(input_functions.store_recipe_by_ingredients(ingredients, recipe_name))
        search_functions.append_record(recipe_by_ingredients)

    elif save == 'n':
        print("Deleting data . . .")
