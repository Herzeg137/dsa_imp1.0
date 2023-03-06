arr = [12,11,13,5,6]

for i in range(1, len(arr)):
  key = arr[i]
  
  #element before the key
  j = i-1
  
  #compare the key with before element
  while j >= 0 and key < arr[j]:
    #if key is smaller than arr[j], set arr[j+1] (key pos) to arr[j] the before element of the key
    arr[j+1] = arr[j]
    #decrease for find the key's actually position in array
    j -= 1
    
  #if the key is not smaller than arr[j], it will the actually position of the key
  arr[j+1] = key
  
  
#print the result array
print(arr)
