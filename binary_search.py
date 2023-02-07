#1 way
def b_s(arr, val):
  low = 0
  high = len(arr) - 1
  
  while low <= high:
    mid = low + (low + high) //2
    guess = arr[mid]
    
    if guess == val:
      return mid
    
    if guess > val:
      high = mid - 1
    
    else:
      low = mid + 1
      
  return None

arr = [....]
b_s(arr, val)


#2 way
def b_s(arr,low, high, val):
  while low <= high:
    mid = low + (low + high) //2
    guess = arr[mid]
    
    if guess == val:
      return mid
    
    if guess > val:
      high = mid - 1
    
    else:
      low = mid + 1
      
  return None

arr = [.....]
b_s(arr, 0, len(arr) - 1, val)
