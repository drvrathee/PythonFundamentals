# if , elif , else statements are used to control the flow of a program based on conditions. They allow you to execute different blocks of code depending on whether a condition is true or false.
"""
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x > y:
    print(f"{x} is greater than {y}")     
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")
"""


# we can also write like 
# if 90 <= score <= 100:
#    print("A")



"""
def main():
    x = int(input("what is x? "))
    if is_even(x):
        print (f"{x} is even")
    else:
        print (f"{x} is odd")

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# or even better 
def is_even(x):
    return x % 2 == 0

main()

"""
# bool only return True of False value. so we can write like this also


# match instead of switch statement in other languages. It is used to match a value against multiple cases and execute the corresponding block of code.
"""
from unittest import case


name = input("Enter your name: ").strip().title() # we can also change logic if suppose we have fullname in match abd the user enters just the first name

match name:
    case "Alice" | "Bobby":  # we can also use | operator to match multiple cases
        print("Hello, Alice!")
    case "Bob":
        print("Hello, Bob!")
    case _:
        print("Hello, stranger!")
"""


print ( "meow\n" * 3 , end = "" )  # end = "" is used to avoid the new line after the print statement. by default it is end = "\n" which means new line. we can also use end = " " to avoid the new line and add a space instead.