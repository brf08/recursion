class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # To insert a new node between node A and B, create a new variable 
    # and store the information about the pointer of B to the variable,
    # set the pointer for the new node to A.next,
    # and set the pointer for B to the (new node).next
    def addNextNode(self, newNode):
        tempNode = self.next
        self.next = newNode
        newNode.next = tempNode

class SinglyLinkedList:
    def __init__(self, arr):
        self.head = Node(arr[0]) if len(arr) > 0 else Node(None)

        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next
    
    def at(self, index):
        iterator = self.head
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None

        return iterator
    
    # Add a new node to the first of the singly linked list
    def preappend(self, newNode):
        newNode.next = self.head
        self.head = newNode
    
    # Add a new node to the last of the singly linked list
    def append(self, newNode):
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        
        iterator.next = newNode

    # Delete (Pop) the first element of the list
    def popFront(self):
        self.head = self.head.next
    
    # Delete the element of the specified index in the list
    def delete(self, index):
        if index == 0: return self.popFront()

        iterator = self.head
        # go to the element of (index-1)
        for i in range(0, index - 1):
            # return null if there is not a next node (out of range)
            if iterator.next == None: return None
            iterator = iterator.next
        
        # iterator -> A(what should be deleted) -> B
        # change the pointer of iterator from A to B
        iterator.next = iterator.next.next
    
    # def reverseHead(self):
    #     if self.head is None or self.head.next is None: return
    #     iterator = self.head
    #     head = iterator.next
    #     iterator.next = None
    #     index = 0
    #     while head.next is not None:
    #         previous = iterator
    #         iterator = head
    #         head = head.next
    #         iterator.next = previous
    #         index += 1
        
    #     previous = iterator
    #     iterator = head
    #     iterator.next = previous
    #     self.head = iterator

    def reverseHead(self):
        if self.head is None or self.head.next is None: return
        reverse = self.head
        self.head = self.head.next
        reverse.next = None
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.next = reverse
            reverse = temp
        
        self.head = reverse


    
    def printList(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.data, end = " ")
            iterator  = iterator.next
        
        print()

numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
numList.printList()

print(numList.at(2).data)

iterator = numList.head
i = 0

while iterator is not None:
    currentNode = iterator
    iterator = iterator.next
    if i % 2 == 0: currentNode.addNextNode(Node(currentNode.data * 2))
    i += 1

numList.printList()
numList.preappend(Node(45))
numList.printList()
numList.append(Node(1234))
numList.printList()
numList.reverseHead()
numList.printList()