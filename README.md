
This repository contains a Python implementation of a doubly linked list with various operations such as adding, removing, and printing nodes.

Classes

Node

The Node class represents a single node in the linked list. It contains the following attributes:


value: The value stored in the node.

parent: A reference to the parent node.

child: A reference to the child node.

LinkedList:
The LinkedList class manages the linked list and provides methods to manipulate it. It contains the following methods:

__init__(self, head=None):
Initializes the linked list. If a head value is provided, it creates the head node; otherwise, the list starts empty.

print(self):
Prints the values of all nodes in the linked list.

printHead(self):
Prints the head node of the linked list.

add(self, value):
Adds a node with the given value to the end of the linked list.

addStart(self, value):
Adds a node with the given value to the start of the linked list.

addNode(self, value, key):
Adds a node with the given value at the position specified by key.

delete(self):
Deletes the last node in the linked list.

remove(self, value):
Removes the first node with the specified value from the linked list.

removePos(self, key)
Removes the node at the position specified by key

Notes
This implementation is intended for educational purposes and may not be optimized for production use.
Future improvements could include error handling, additional features, and performance optimizations.
