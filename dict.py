# dict is a collection of key-value pairs. It is a mutable data type, which means we can change the elements of the dict after it has been created. 
# Dicts are defined by enclosing a comma-separated sequence of key-value pairs in curly braces {}. Each key is separated from its value by a colon :.
# The keys in a dict must be unique and immutable (e.g., strings, numbers, tuples)
"""
students = {  # basically key value pairs. key is the name of the student and value is the house of the student.
    "hermione": "gryffindor",
    "harry": "gryffindor",
    "ron": "gryffindor",
    "draco": "slytherin"
}

print(students["hermione"])  # we can access the value of a key by using the key in square brackets. here it will print gryffindor
# but this is manual , 

# lets make it dynamic

for student in students:
    print(student, students[student], sep=": ")  # here we are iterating through the keys of the dict and printing the key and its value. it will print all the students and their houses.
"""

students = [  # a list of dictionaries containig name , house , patronous and anything else
    {"name": "Hermione" , "house" : "Gryffindor" , "patronus" : "Otter"},
    {"name":"Harry" , "house": " Gryffindor" , "patronus" : "Stag"},
    {"name" : "Draco" , "house" : "Slytherin" , "patronus" : None} # None keyword means no value for this key
]


for student in students:
    print(student["name"], student["house"], student["patronus"] , sep=", ")
 