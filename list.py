# list is a collection of items in a particular order. It is a mutable data type, which means we can change the elements of the list after it has been created. Lists are defined by enclosing a comma-separated sequence of items in square brackets [].

#students=["hermione","harry","ron"]

#for i in range(len(students)):# len returnt the length of the list and we pass that int to range function to get the index of the list. 
#    print(i+1 , students[i]) # now i knows the length of the list and prints each element.

"""
helist = ["apple" , 'banana', "mango" , "pear"]

#print( helist)

#for i in range(len(helist)):
#    print(helist[i])


#for i, item in enumerate(helist):
#    print(i+1, item)

j = len(helist) - 1
while j>=0:
    print(helist[j])
    j-=1 

"""

leest = [1,2,3]

leest.append("hi")

leest.insert(0, "hello") # insert method takes two arguments, first is the index where we want to insert the element and second is the element we want to insert.

leest.remove(3) # remove method removes the first occurrence of the specified element from the list.

print(leest)

