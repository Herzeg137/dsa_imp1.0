class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue_structure:
    def __init__(self):
        self.head = None
        self.last = None
    
    #enQueue() -> oxiriga qo'shish.
    def enQueue(data):
        if last is None:
            head = Node(data)
            last = head
        else:
            last.next = Node(data)
            last = last.next
    
    #deQueue -> boshidan o'chiradi.
    def deQueue(self):
        if head is None:
            return None
        else:
            val_return = head.data
            head = head.next
            return val_return
        
    #isEmpty -> queue Empty ekanligini tekshiradi.
    def isEmpty(self):
        if head is None:
            return True
        else:
            return False
    
    #isFull -> queue Full ekanligini tekshiradi.
    def isFull(self):
        if not isEmpty():
            return True
        else:
            return False
