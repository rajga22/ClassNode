class Node:
def __init__(self, value, parent, child):
self.value = value
self.parent = parent
self.child = child

class LinkedList():
def __init__(self, head=None):
if head is None:
self.head = None
else:
self.head = Node(head, None, None)
def print(self):
node = self.head
while node:
print(node.value, end=" ")
node = node.child
print()
def printHead(self):
print(self.head)
def add(self, value):
node = self.head
if node is None:
newNode = Node(value, None, None)
self.head = newNode
else:
if self.head.child:
while node.child:
node = node.child
newNode = Node(value,node,None)
node.child = newNode
else:
newNode = Node(value, self.head, None)
self.head.child = newNode
def addStart(self, value):
if self.head is None:
newNode = Node(value, None, None)
else:
newNode = Node(value, None, self.head)
self.head.parent = newNode
self.head = newNode
def addNode(self, value, key):
node = self.head
for i in range(int(key)-1):
node = node.child
newNode = Node(value, node, node.child)
node.child = newNode
if newNode.child is not None:
newNode.child.parent = newNode
def delete(self):
node = self.head
while node.child:
node = node.child
node.parent.child = None
def remove(self, value):
node = self.head
while node.child:
if node.value == value:
if node == self.head:
node.child.parent = None
self.head = node.child
else:
node.parent.child = node.child
node.child.parent = node.parent
break
else:
node = node.child
def removePos(self, key):
node = self.head
for i in range(int(key)-1):
node = node.child
node.child = node.child.child
node.child.parent = node