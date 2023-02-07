#1 way
def l_s(arr, val):
  for i in range(len(arr)):
    if arr[i] == val:
      return i
  return None

#2 way
def l_s(arr, val):
  i = 0
  n = len(arr)
  
  if i > n:
    return "Not found"
  
  elif arr[i] == val:
    return i
    i += 1

arr = [.......]
l_s(arr, val)
