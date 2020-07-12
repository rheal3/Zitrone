import os
# os.system('clear')


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

    ingredients_list = gather_ingredients()

    os.system('clear')

    print("Now that we've entered the ingredients, let's type in the method.")
    print("Once again you can type in 'done' when you are finished.")

    recipe_steps = gather_recipe_steps()

    os.system('clear')

    print("Compiling recipe . . .")

    compiled_recipe = format_recipe(recipe_name, ingredients_list, recipe_steps)

    print(compiled_recipe)

    save = input("\nWould you like to save the recipe to your database? (y/n) ")

    if save == 'y':
        save_recipe(os.path.join('./recipe_database/', recipe_name.lower()), compiled_recipe)
        print("Your recipe has been saved.")

    else:
        print("Deleting data.")




elif choice == 'database':
    os.system('clear')
    print("Accessing data . . . ")

    database_list = []

    for root, directories, files in os.walk('./recipe_database/'):
        for file in files:
            database_list.append(os.path.join('./recipe_database/', file))

    for i in range(0, len(database_list)):
        database_list[i] = database_list[i].replace("./recipe_database/", "").replace(".txt", "").lower()
        print(database_list[i].title())

    access = input("\nWould you like to access a recipe? (y/n) ")
    if access == 'y':
        recipe_to_access = input("Which recipe would you like to access? ")
        if recipe_to_access.lower() in database_list:
            file_to_open = open(os.path.join('./recipe_database/', database_list[database_list.index(recipe_to_access)] + '.txt'), 'r')
            for line in file_to_open:
                print(line, end="")
            print("\n")


    elif access == 'n':
        input("Type 'main' to return to the main menu. ")
    else:
        print("Command not understood.")
        input("Enter a valid command. ")


elif choice == 'help':
    pass
else:
    print("That is not a valid command.")
