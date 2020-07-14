import os
import functions
import time

# Main Code

choice = functions.main()

while choice != 'exit':

    if choice == 'input':
        os.system('clear')

        print("I see you've decided to input a recipe!")
        recipe_name = input("What is the name of the recipe? ").title()

        os.system('clear')

        print("Sounds delicious!")
        print("Now let's enter some ingredients. We'll enter the ingredients first and then the amount that we need after.")
        print("When you finish type 'done' to move to the next step.")

        ingredients = functions.gather_ingredients()

        os.system('clear')

        print("Now that we've entered the ingredients, let's type in the method.")
        print("Once again you can type in 'done' when you are finished.")

        recipe_steps = functions.gather_recipe_steps()

        os.system('clear')

        print("Compiling recipe . . .")

        compiled_recipe = functions.format_recipe(recipe_name, ingredients, recipe_steps)

        print(compiled_recipe)

        save = input("\nWould you like to save the recipe to your database? (y/n) ")

        if save == 'y':
            if not os.path.exists('./recipe_database'):
                os.makedirs('./recipe_database')
            functions.save_recipe(os.path.join('./recipe_database', recipe_name.lower()), compiled_recipe)

            print("Your recipe has been saved.")

            recipe_by_ingredients = functions.store_recipe_by_ingredients(ingredients, recipe_name)

            time.sleep(1)
            choice = functions.main()

        else:
            print("Deleting data . . .")

            time.sleep(1)
            choice = functions.main()



    elif choice == 'database':
        os.system('clear')
        print("Accessing data . . . \n")
        time.sleep(.5)
        database_list = [os.path.join('./recipe_database/', file) for root, directories, files in os.walk('./recipe_database/') for file in files]

        if len(database_list) > 0:

            functions.list_of_recipes(database_list)

            access = input("Would you like to access a recipe? (y/n) ")
            while access == 'y':
                access = functions.open_recipe(database_list)
                if access != 'n':
                    os.system('clear')
                    functions.list_of_recipes(database_list)

            if access == 'n':
                print("Returning to main menu . . .")
                time.sleep(1)
                choice = functions.main()
            else:
                print("Command not understood.")
                input("Enter a valid command. (y/n) ")
        else:
            print("There are currently no recipes in your database.")
            time.sleep(1)
            choice = functions.main()



    elif choice == 'help':
        os.system('clear')
        functions.help()
        choice = input("What would you like to do? ")
    else:
        print("That is not a valid command.")
        time.sleep(1)
        choice = functions.main()
