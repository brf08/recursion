class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueueFront(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node

    def enqueueBack(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeueFront(self):
        if self.head == None: return None
        
        temp = self.head
        self.head = self.head.next
        if self.head is not None: self.head.prev = None
        else: self.tail = None
        
        return temp.data
    
    def dequeueBack(self):
        if self.tail == None: return None
        
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail is not None: self.tail.next = None
        else: self.head = None
        
        return temp.data

    def peekFront(self):
        if self.head == None: return None
        return self.head.data

    def peekBack(self):
        if self.tail == None: return self.peekFront()
        return self.tail.data
    
    def printList(self):
        iterator = self.head
        while iterator != None:
            print(iterator.data, end = " ")
            iterator = iterator.next
        print()



q = Deque()
print(q.peekFront())
print(q.peekBack())

q.enqueueFront(10)
q.enqueueFront(20)
print(q.peekFront())
print(q.peekBack())

q.enqueueBack(30)
q.enqueueBack(40)
print(q.peekFront())
print(q.peekBack())
q.printList()

q.dequeueFront()
q.printList()

q.dequeueBack()
q.printList()

def getMax(arr):
    deque = Deque()
    deque.enqueueFront(arr[0])

    for i in arr[1:]:
        if i > deque.peekFront(): deque.enqueueFront(i)
        else: deque.enqueueBack(i)

    deque.printList()
    return deque.peekFront()

print(getMax([34,35,64,34,10,2,14,5,353,23,35,63,23]))

def getMaxWindows(arr, k):
    if k > len(arr): return []

    results = []
    # dequeには、ウィンドウ内の要素となるarrのインデックスがはいる
    deque = Deque()

    # dequeの初期化
    for i, num in enumerate(arr[:k]):
        #print("num is " + str(num) + ", deque.peekback() is " + str(arr[deque.peekBack()]))
        
        # 新しい値と既存の値を比較し、既存の値が新しい値以下であれば、末尾からすべて削除
        # 結果として、dequeの先頭の値がインデックスであるarrの要素はウィンドウ内の最大値となる
        while deque.peekBack() is not None and arr[deque.peekBack()] <= num:
            deque.dequeueBack()
        
        deque.enqueueBack(i)
        deque.printList()

    for i, num in enumerate(arr[k:], k):
        # 最大値であるdequeの先頭に相当するarr要素をresultsへ
        results.append(arr[deque.peekFront()])
        # ウィンドウ外の要素は取り除く
        while deque.peekFront() is not None and deque.peekFront() <= i-k:
            deque.dequeueFront()
        # 新しい値と既存の値を比較し、既存の値が新しい値以下であれば、末尾からすべて削除
        while deque.peekBack() is not None and arr[deque.peekBack()] <= num:
            deque.dequeueBack()
        
        deque.enqueueBack(i)
        print("i-k is " + str(i-k) + ", deque.peekFront() is " + str(deque.peekFront()))
        deque.printList()

    results.append(arr[deque.peekFront()])

    return results

print(getMaxWindows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4))
        




# getMaxWindows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4); #[64, 64, 64, 34, 14, 353, 353, 353, 353, 63]