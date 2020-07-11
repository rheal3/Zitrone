

def gather_ingredients():
    ingredients = {}
    ingredient = ""
    while ingredient != "done":
        ingredient = input("Ingredient: ")
        if ingredient == "done":
            return ingredients
        amount = input(f"Amount of {ingredient}: ")
        ingredients[ingredient] = amount

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
    print(f"\n{recipe_name.title()}")
    print("\nIngredients:")
    for ingredient, amount in recipe_ingredients.items():
        print(f"{amount:<8} {ingredient.lower()}")
    print("\nSteps: ")
    for count, step in recipe_steps.items():
        print(f"Step {count}:  {step}")

def save_recipe(recipe_name, compiled_recipe):
    text_file = open(f"{recipe_name}.txt", "w")
    text_file.write(compiled_recipe)
    text_file.close()




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
    print("I see you've decided to input a recipe!")
    recipe_name = input("What is the name of the recipe? ")

    print("Sounds delicious!")
    print("Now let's enter some ingredients. We'll enter the ingredients first and then the amount that we need after.")
    print("When you finish type 'done' to move to the next step.")

    ingredients_list = gather_ingredients()

    print("Now that we've entered the ingredients, let's type in the method.")
    print("Once again you can type in 'done' when you are finished.")

    recipe_steps = gather_recipe_steps()

    print("Compiling recipe . . .")

    compiled_recipe = format_recipe(recipe_name, ingredients_list, recipe_steps)

    print(compiled_recipe)

    save = input("Would you like to save the recipe to your database? (y/n) ")

    if save == 'y':
        save_recipe(recipe_name, compiled_recipe)
        print("Your recipe has been saved.")
    else:
        print("Deleting data.")

















elif choice == 'database':
    pass
elif choice == 'help':
    pass
else:
    print("That is not a valid command.")
