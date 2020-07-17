import os


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
        {0}search{1}: search for recipes using specific ingredients
        {0}help{1}: view list of commands""".format('\033[1m', '\033[0m'))
    return input("What would you like to do (input / database / search / help / exit)? ").lower().strip()


# Help Functions
def help():
    os.system('clear')
    print("I see you've found the tremendously helpful help page!")
    print("""List of Commands:
    Commands To Get Places:
        {0}exit{1}: exit the program
        {0}input{1}: input a new recipe
        {0}database{1}: view a list of all of your inputted recipes
        {0}help{1}: view this list of the commands
    Commands In Those Places:
        {0}done{1}: anytime you have finished inputting ingredients you will type in done to let the computer know
        {0}y{1} or {0}n{1}: periodically the app will ask you a yes or no question (y/n) you can answer this by typing in y or n
    Don't worry if you can't remember them all right now.
    There are instructions within the different portions of the app to remind you of what you can do.""".format('\033[1m', '\033[0m'))

# sys.argv About Function:
def about():
    os.system('clear')
    print("""
    {0}Zitrone?{1}
        I call it the 'lemon in cut tobacle'. I'm sure you all know what I mean. You're going along happy as ever ~tralala~ and decide that you'd like to snazz up your water with some lemon. A seemingly innocent task shrouded in potential pain. I'll give you some examples: there's the 'lemon in eye snapfoo', the 'too much lemon in mouth sour face' (aka. sour doom, aka. contorted pain), and of course today's mortal blow... the 'lemon in cut tobacle'. The lemon was cut and the squeezing had begun when all of a sudden the burning began. The lemony fluids had oozed into a sliver of a cut on the palm of my knuckle. It. Was. Agony. The trauma of the whole experience remained with me and so, as any sane individual would do, I decided to name my app after this fiendish fruit's German counterpart ~Zitrone~.

    {0}How Zitrone Came To Be...{1}
        A long long time ago in a kitchen not so unlike your own sat a girl trying to decide what to make for dinner. There were vegetables in the fridge, and grains in the pantry, but the recipes that used them were hard to find. :( The girl made a wish. A wish to be able to type in ingredients to an app and have recipes appear. She wished and she wished and she wished. Then, one day, she stopped wishing. She had acquired the know how to make an app for herself and that's exactly what she did. Of course there was the 'lemon in cut tobacle' and much googling involved before her toils were rewarded with the app you find yourself using today.

    {0}How Zitrone Can Help You...{1}
        Zitrone in an app that allows you to input your own recipes and store them to a personal database. However, the coolest part of the app is the search feature. Using this, you can input any ingredient you have on hand (that's in your list of ingredients stored from your recipe input) and out will come a list of recipes that use the ingredients. WARNING: This feature may reduce food waste in your home!
        """.format('\033[1m', '\033[0m'))
