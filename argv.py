# sys.argv is a list in Python, which contains the command-line arguments passed to the script. With the first item in this list being the name of the script itself, and the rest being the additional arguments provided by the user.

# For example, if you run a script like 'python script.py arg1 arg2',

# import sys 

# sys.argv[0] is the name of the script when run via command line. so python argv.py will return argv.py

# print("hello , my name is ", sys.argv[1])  # This will print the first argument passed to the script.

# so if we run the script like 'python argv.py John', it will print "hello , my name is John"

# suppose we do python name.py 

# print("hello , my name is ", sys.argv[1]) This will print the first argument passed to the script 
# in this case it will throw an error because we did not pass any argument to the script. so it will give an index error because sys.argv[1] does not exist.

# sys.exit() is a function in the sys module that allows you to exit from Python. It can be used to terminate the program and optionally pass an exit status code back to the operating system. .


"""
import sys
if len(sys.argv) < 2:  # Check if the number of command-line arguments is less than 2
    sys.exit("Too few arguments")  # Exit the program with a message if there are too few arguments

for arg in sys.argv[1:-1]:#-1 will remove 1 arg from the end  # Iterate over the command-line arguments starting from the second one till the second last, this is called slicing .
    print("hello , my name is ", arg)  # Print a greeting for each argument passed to the script

"""

""" 

PACKAGES , we can get from PyPi to download and get all kinds of packages

niowadays we use pip , which is a python package manager

"""

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

