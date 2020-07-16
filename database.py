import os

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
