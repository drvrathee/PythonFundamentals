# Python does not have a built in linked list like java or c++ . 
# we create a class of node and join noedes together 

# List vs linked list trade offs
# #You already know arrays (Python lists). A list keeps its items side by side in memory:
#That makes arr[2] instant, because Python can work out exactly where index 2 is. But inserting at the front is slow. Every item has to shift one place right to make room, so the cost is O(n).
#A linked list gives up instant indexing so that inserting and deleting become cheap. Its items can sit anywhere in memory. Each item holds its value plus an arrow pointing to the next item:


# Singly linked list

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def insert_after(self, new_node):
        new_node.next = self.next
        self.next = new_node
