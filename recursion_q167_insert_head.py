class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self, arr):
        if len(arr) <= 0:
            self.head == SinglyLinkedListNode(None)
            return

        self.head = SinglyLinkedListNode(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = SinglyLinkedListNode(arr[i])
            currentNode = currentNode.next
        
        
def insertAtHead(head,data):
    newNode = SinglyLinkedListNode(data)
    newNode.next = head
    head = newNode
    return head

insertAtHead(singlyLinkedList([3,3,2,10,34,45,67,356]),367)