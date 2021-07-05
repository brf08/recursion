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