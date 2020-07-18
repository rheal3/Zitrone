import json
import os

# Search Functions
def append_record(dictionary):
    with open('ingredient_search', 'a') as file:
        json.dump(dictionary, file)
        file.write(os.linesep)

def access_record():
    ingredients_dictionary = {}
    try:
        with open('ingredient_search') as file:
            record_list = [json.loads(line) for line in file]
            for line in record_list:
                for key, value in line.items():
                    if key not in ingredients_dictionary:
                        ingredients_dictionary[key] = value
                    else:
                        ingredients_dictionary[key.lower()] += value
        return ingredients_dictionary
    except:
        return "Error."

def search_by_ingredient(ingredient_to_find, ingredient_search):
    recipes_with_ingredient = []
    for ingredient in ingredient_search:
        if ingredient == ingredient_to_find:
            recipes_with_ingredient += ingredient_search[ingredient]
    return recipes_with_ingredient

def sort_recipes_by_most_ingredients(recipes_mult_ingredients):
    highest_value_recipe = ""
    highest_value = 0
    for recipe, ingredients in recipes_mult_ingredients.items():
        if len(ingredients) > highest_value:
            highest_value = len(ingredients)
            highest_value_recipe = recipe
    print(f"{highest_value_recipe} - {recipes_mult_ingredients[highest_value_recipe]}")
    del recipes_mult_ingredients[highest_value_recipe]
    return recipes_mult_ingredients

def create_search_database_list(recipes_mult_ingredients_copy, database_list):
    search_database_list = []
    if len(recipes_mult_ingredients_copy) > 0:
        for recipe_name, ingredients in recipes_mult_ingredients_copy.items():
            search_path = f"./recipe_database/{recipe_name.lower()}.txt"
            index = database_list.index(search_path)
            search_database_list += [database_list[index]]
    return search_database_list
