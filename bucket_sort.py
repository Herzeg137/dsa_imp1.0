#it works just for float and int, not for negative.
def bucketsort(arr, noOfBuckets):
    max1, min1 = max(arr), min(arr)
    rnge = (max1 - min1) / noOfBuckets
    temp = []

    #create empty buckets
    for _ in range(noOfBuckets):
        temp.append([])

    #scatter into buckets
    for i in range(len(arr)):
        diff = (arr[i] - min1) / rnge - int((arr[i] - min1) / rnge)
    
        #append to subarray
        if (diff == 0 and arr[i] != min1):
            temp[int( ( arr[i] - min1) / rnge ) - 1].append(arr[i])
        
        else:
            temp[int( ( arr[i] - min1 ) / rnge )].append(arr[i])
    
    #sort each bucket
    for j in range(len(temp)):
        if len(temp[j]) != 0:
            temp[j].sort()

    #concatenate
    k = 0
    for lst in temp:
        if lst: #if subarray is empty in this condition result will be False, otherwise True
            for i in lst:
                arr[k] = i
                k += 1

    #return the sorted arrays
    return temp


#Driver code
arr = [ 9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
noOfBuckets = 5
print(bucketsort(arr, noOfBuckets))
