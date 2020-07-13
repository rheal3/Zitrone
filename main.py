import os
import functions


# Main Code
os.system('clear')

print("""Welcome to {}!
This is an app that allows you to create recipes and store them in your own personal database.
Let's get started!
To begin you're going to need to know a few simple commands:
To input a new recipe you will use the 'input' command.
If you want to view your database of recipes you can do so by typing 'database' command.
If you ever need help, you can type in the 'help' command.
And if you want to come back here to the main screen just type the 'exit' command.
When you're done looking at your recipes you can always exit the application entirely using CTRL + C .""")

choice = input("What would you like to do? ")

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

    else:
        print("Deleting data.")




elif choice == 'database':
    os.system('clear')
    print("Accessing data . . . ")

    database_list = []

    for root, directories, files in os.walk('./recipe_database/'):
        for file in files:
            database_list.append(os.path.join('./recipe_database/', file))

    if len(database_list) > 0:

        for i in range(0, len(database_list)):
            database_list[i] = database_list[i].replace("./recipe_database/", "").replace(".txt", "").lower()
            print(database_list[i].title())

        access = input("\nWould you like to access a recipe? (y/n) ")
        if access == 'y':
            functions.access_recipe(database_list)
            # Would you like to access another recipe?

        elif access == 'n':
            input("Type 'main' to return to the main menu. ")
        else:
            print("Command not understood.")
            input("Enter a valid command. ")

    else:
        print("There are currently no recipes in your database.")
            # Return to main and input to create.



elif choice == 'help':
    pass
else:
    print("That is not a valid command.")
