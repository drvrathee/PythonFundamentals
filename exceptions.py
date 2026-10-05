#try:
#    x= int(input("Please enter a number: "))
#    print(f"You entered: {x}")
#except ValueError:
#    print("Invalid input! Please enter a valid integer.") 


def get_int():
    while True:

        try:
            x = int(input("Please enter a number: "))
            return x
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# pass is used with except when you want to ignore the exception and continue execution without any action. It allows the program to continue running without raising an error or stopping execution.
# like except ValueError:
#           pass  ---- so we catched the exception but instead of prompting something we let it pass


def main():
    x=get_int("What's x? ")
    print(f"You entered: {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# we can also use 'raise' keyword and raise an exception to indicate that an error has occurred. This can be useful for propagating errors up the call stack or for creating custom exceptions.

