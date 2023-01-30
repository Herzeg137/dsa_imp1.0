#push() => Top ga element qo'shib tepaga ko'tariladi.
def push(val, size):
    if top == size:
        return "Overflow"
    top += 1
    stack[top] = val

#pop( => Top dagi element ni tashlab yuborib pasga tushadi.
def pop():
    if top == -1:
        return "Underflow"
    else:
        top -= 1
        
#peek() => top dagi elementni chiqazadi.
def peek():
    if top == -1:
        return "Underflow"
    else:
        return stack[top]

#isFull() => stack full ligini tekshiradi. 
def isFull():
    if top == size - 1:
        return True
    else:
        return False
#isEmpty() => stack empty ekanligini tekshiradi.
def isEmpty():
    if top == -1:
        return True
    else:
        return False
