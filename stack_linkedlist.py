#Note: LL da top belgini head ga o'zgartirib turamiz.

#push() => LinkedList ning boshiga yangi element qo'shadi.
def push(val: int):
    #create a new node
    newNode.data = val
    
    #make the newnode points to the head node
    newNode.next = head
    
    #make the new node as the head node.
    head = newNode

#pop() => LL ning boshidagi element ni o'chiradi.    
def pop():
    #assign the head. because we will delete the head
    poppednode = head
    
    #traverse the LinkedList
    head = head.next
    
    #separate the poppednode(head / top item)
    poppednode.next = None
    
    #get the popped item
    return poppednode.data

#peek() => get head item
def peek():
    return head.data

#isEmpty() => LL Empty ligini tekshiradi.
def isEmpty():
    if head == None:
        return True
    else:
        return False
