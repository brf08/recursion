class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    
    def pop(self):
        if self.head == None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None: return None
        return self.head.data
    
def reverse(arr):
    stack = Stack()
    for i in arr:
        stack.push(i)

    reversed = []
    while stack.peek() is not None:
        reversed.append(stack.pop())
    return reversed

def consecutiveWalk(arr):
    stack = Stack()
    stack.push(arr[0])
    for i in arr[1:]:
        if stack.peek() < i:
            while stack.peek() is not None: stack.pop()
        stack.push(i)
    
    results = []

    while stack.peek() is not None: results.insert(0, stack.pop())
    return results

def consecutiveIncreaseWalk(arr):
    stack = Stack()
    stack.push(arr[0])
    for i in arr[1:]:
        if stack.peek() > i:
            while stack.peek() is not None: stack.pop()
        stack.push(i)

    results = []

    while stack.peek() is not None: results.insert(0, stack.pop())
    return results
    

# arr = [1, 2, 3, 4, 5, 6]
# print(reverse(arr))   

print(consecutiveWalk([3,4,20,45,56,6,4,3,5,3,2])) # [5,3,2]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54])) # [64,3,0,-34,-54]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54,4])) # [4]
print(consecutiveIncreaseWalk([3,4,20,45,56,6,4,3,2,3,9])) # [2,3,9]
print(consecutiveIncreaseWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54])) # [-54]
print(consecutiveIncreaseWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54,4])) # [-54,4]