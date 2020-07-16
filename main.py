import os
import functions
import database
import search_ingredient
import input_recipe
import time

# Main Code
choice = functions.main()

while choice != 'exit':

    if choice == 'input':
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

        ingredients = input_recipe.gather_ingredients()

        os.system('clear')

        print("Now that we've entered the ingredients, let's type in the method.")
        print("Once again you can type in {0}'done'{1} when you are finished.".format('\033[1m', '\033[0m'))

        recipe_steps = input_recipe.gather_recipe_steps()

        os.system('clear')

        print("Compiling recipe . . .")

        compiled_recipe = input_recipe.format_recipe(recipe_name, ingredients, recipe_steps)

        print(compiled_recipe)

        save = input("\nWould you like to save the recipe to your database? (y/n) ").lower().strip()
        while save != 'y' and save != 'n':
            print("Command not understood.")
            save = input("Enter a valid command. (y/n) ").lower().strip()

        if save == 'y':
            if not os.path.exists('./recipe_database'):
                os.makedirs('./recipe_database')
            input_recipe.save_recipe(os.path.join('./recipe_database', recipe_name.lower()), compiled_recipe)
            print("Your recipe has been saved.")
            recipe_by_ingredients = {}
            recipe_by_ingredients.update(input_recipe.store_recipe_by_ingredients(ingredients, recipe_name))
            search_ingredient.append_record(recipe_by_ingredients)
            time.sleep(1)
            choice = functions.main()

        elif save == 'n':
            print("Deleting data . . .")

            time.sleep(1)
            choice = functions.main()



    elif choice == 'database':
        database_list = [os.path.join('./recipe_database/', file) for root, directories, files in os.walk('./recipe_database/') for file in files]
        os.system('clear')
        print("Accessing database . . . \n")
        time.sleep(.5)

        if len(database_list) > 0:

            database.list_of_recipes(database_list)

            access = input("Would you like to view a recipe? (y/n) ").lower().strip()
            while access == 'y':
                access = database.open_recipe(database_list)
                if access != 'n':
                    os.system('clear')
                    database.list_of_recipes(database_list)

            if access == 'n':
                print("Returning to main menu . . .")
                time.sleep(1)
                choice = functions.main()
            else:
                print("Command not understood.")
                access = input("Enter a valid command. (y/n) ").lower().strip()
        else:
            print("There are currently no recipes in your database.")
            time.sleep(1)
            choice = functions.main()


    elif choice == 'search':
        database_list = [os.path.join('./recipe_database/', file) for root, directories, files in os.walk('./recipe_database/') for file in files]
        if len(database_list) > 0:
            continue_search = True

            while continue_search == True:
                os.system('clear')
                print("Here you may search for a specific recipe or search for an ingredient and see which recipe has it!")
                print("This is a list of all the ingredients you can search with: \n")
                ingredient_search = search_ingredient.access_record()

                if ingredient_search == "Error.":
                    print("This feature is unavailable at this time. Please try again later.")
                    time.sleep(2)
                    continue_search = False
                    choice = functions.main()
                    continue

                ingredient_list = [ingredient for ingredient, recipe in ingredient_search.items()]
                print(ingredient_list, '\n')
                print("You can search using multiple ingredients. Type {0}'done'{1} when you're done. ".format('\033[1m', '\033[0m'))

                recipes_mult_ingredients = {}
                ingredient_to_find = ""
                ingredient_to_find_list = []

                while ingredient_to_find.strip().lower() != 'done':
                    ingredient_to_find = input("Type in the ingredient you would like to use: ").lower().strip()
                    if ingredient_to_find == 'done':
                        continue
                    ingredient_to_find_list.append(ingredient_to_find)
                    recipes_with_ingredient = search_ingredient.search_by_ingredient(ingredient_to_find, ingredient_search)

                    for recipe in recipes_with_ingredient:
                        if recipe not in recipes_mult_ingredients:
                            recipes_mult_ingredients[recipe] = 1
                        else:
                            recipes_mult_ingredients[recipe] += 1

                os.system('clear')
                print("Searching database . . .")
                time.sleep(.5)
                print("Here is a list of recipes using: {} ordered by most ingredients used.\n".format(', '.join(ingredient_to_find_list)))

                while len(recipes_mult_ingredients) > 0:
                    highest_value_recipe = search_ingredient.sort_recipes_by_most_ingredients(recipes_mult_ingredients)
                    print(highest_value_recipe)
                    del recipes_mult_ingredients[highest_value_recipe]

                choice = input("\nWould you like to make another search? (y/n) ")
                if choice == 'y':
                    choice = 'search'
                else:
                    continue_search = False
                    choice = functions.main()

        else:
            print("There are currently no recipes in your database to search from.")
            time.sleep(1)
            choice = functions.main()


    elif choice == 'help':
        os.system('clear')
        functions.help()
        choice = input("What would you like to do? ").lower().strip()

    else:
        print("That is not a valid command.")
        time.sleep(1)
        choice = functions.main()
