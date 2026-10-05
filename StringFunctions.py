
# BASIC STRING FUNCTION 

#input function

name = input("What is your name? ").strip().title()



# splits the inout of name variables and stores the first and last name in two different variables

#firstname , lastname = name.split(" ")

#Strips extra white spaces from front and back

#name = name.strip()

# makes First letter of string capital
#name = name.capitalize()
# name.upper() for all caps 



#Replace all spaces in the string with underscores. or replace some alphabet or phrase with something
#name = name.replace(" ", "_")

#name = name.strip().capitalize()   like this functions can form like a chain and do everythign in one go

# we could lso add all strip and title finction in the input line


Dhruv
print(f"Hello, {name}!")



# string methods 

#.strip()
#.join()



raw = " chikEn tikKa Masala"

query = raw.strip().lower().capitalize()

print (query)
 
