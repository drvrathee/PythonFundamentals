# importing file a_test.py
""""
p = open("a_test.py", "r")  # open file in read mode

print(p.read())  # read the file and print its content

p.close()  # close the file

"""

with open("a_test.py", "r") as p:  # open file in read mode using 'with' statement
    print(p.read())  # read the file and print its content
# or another way to read the file using 'with' statement

with open("a_test.py", "r") as p:  # open file in read mode using 'with' statement
    for line in p:  # iterate through each line in the file
        print(line.strip())  # print each line after stripping whitespace


# now write in file and creatigna  new file

with open("new_file.py", "w") as f:  # open file in write mode
    f.write("# This is a new file created using write mode\n")  # write content to the file
    f.write("print('Hello, World!')\n")  # write another line to the file

