class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self,arr):
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return

        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        self.tail = currentNode

    def at(self, index):
        iterator = self.head
        for i in range (0, index):
            iterator = iterator.next
            if iterator == None: return None
        
        return iterator
    
    # add the new node to the first of the list
    def preappend(self, newNode):
        self.head.prev = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode

    # add the new node to the last of the list
    def append(self, newNode):
        self.tail.next = newNode
        newNode.prev = self.tail
        newNode.next = None
        self.tail = newNode
    
    # add the new node to the next of the specified node
    def addNextNode(self, node, newNode):
        tempNode = node.next
        node.next = newNode
        newNode.next = tempNode
        newNode.prev = node
        
        if node is self.tail: self.tail = newNode
        else: tempNode.prev = newNode
    
    # pop the first node from the list
    def popFront(self):
        self.head = self.head.next
        self.head.prev = None

    # pot the last node from the list
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None

    # delete the specified node from the list
    def deleteNode(self, node):
        if node is self.tail: return self.pop()
        if node is self.head: return self.popFront()

        node.prev.next = node.next
        node.next.prev = node.prev
    
    def reverse(self):
        reverse = self.tail
        iterator = self.tail.prev

        currentNode = reverse
        while iterator is not None:
            currentNode.next = iterator

            iterator = iterator.prev
            if iterator is not None: iterator.next = None

            currentNode.next.prev = currentNode
            currentNode = currentNode.next
        
        self.tail = currentNode
        self.head = reverse
        self.head.prev = None
    
    def printInReverse(self):
        iterator = self.tail
        while(iterator != None):
            print(iterator.data, end = " ")
            iterator = iterator.prev
        print()
    
    def printList(self):
        iterator = self.head
        while(iterator != None):
            print(iterator.data, end = " ")
            iterator = iterator.next
        print()

numList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])

numList.printList()
print(numList.head.data)
print(numList.head.next.data)
print(numList.tail.data)
print(numList.tail.prev.data)
print(numList.at(0).data)
print(numList.at(2).data)
print(numList.at(12).data)

numList.printInReverse()

numList.printList()
numList.reverse()
numList.printList()
numList.printInReverse()

# 45をpreappend
numList.preappend(Node(45))
print(numList.head.data)
numList.printList()

# 71をappend
numList.append(Node(71))
print(numList.tail.data)
numList.printList()
print("")

# ノードの後に新しいノードを追加
numList.addNextNode(numList.at(3), Node(4))
numList.printList()
print(numList.tail.data)

numList.addNextNode(numList.at(15), Node(679))
numList.printList()
print(numList.tail.data)

numList.printInReverse()

print("Deleting in O(1)")
numList.printList()

numList.deleteNode(numList.at(3))
numList.deleteNode(numList.at(9))
numList.deleteNode(numList.at(0))

numList.printList()
numList.printInReverse()