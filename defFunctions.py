"""def main():
    name = input("What is your name? ").strip().title()
    hello(name) # name in main function , to in hello function


def hello(to="World"):
    print(f"Hello, {to}!") # we can't use name variable in hello function because it is not defined in this function. it is put of scope of this function. so we need to pass it as an argument to hello function.

main()
"""

def main():
    x = int(input("what is x? "))
    print("square of x is ",  square(x))


def square (x):
    return x * x # or power(x, 2) or x ** 2

main()
