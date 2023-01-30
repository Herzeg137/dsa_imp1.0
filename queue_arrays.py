#enQueue -> queue ning oxiriga element qo'shish.
def enQueue(val: int):
    if (rear + == size):
        return "Overflow"
    else:
        if front == -1 and rear == -1:
            front = 0
            rear = 0
        else:
            rear += 1
            
        queue[rear] = val
        
#deQueue -> queue ning boshidan element o'chirish.
def deQueue():
    if front == -1 or front > rear:
        return "Underflow"
    else:
        y = queue[front]
        if front == rear:
            front = rear = -1
        else:
            front += 1
        
        return y
    
#isFull() -> queue Full ekanligini tekshiradi.
def isFull():
    if rear = size - 1:
        return True # "Overflow condition"
    else:
        return False
    
#isEmpty(): -> queue Empty ekanligini tekshiradi.
def isEmpty():
    if front == -1 or front > rear:
        return True # "Underflow condition"
    else:
        return False
