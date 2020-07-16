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
    print("I see you've found the tremendously helpful help page!")
    print("""List of Commands:
        {0}exit{1}: exit the program
        {0}input{1}: input a new recipe
        {0}database{1}: view a list of all of your inputted recipes
        {0}help{1}: view this list of the commands""".format('\033[1m', '\033[0m'))
    # print("""About Zitrone:
    # Zitrone allows you to input your recipes and store them to a database.""")
