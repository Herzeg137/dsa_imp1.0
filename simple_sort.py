def simple_sort(A):
  out = [0] * len(A)
  
  for i in range(len(A)):
    out[A[i]] = A[i]  
  
  return out


#driver code
A = [1,5,0,3,6,4,2]
simple_sort(A)


"""
All we have to do is map each element A[i] to index A[i] in the output array. This algorithm runs in O(N) time and O(N) extra space. 
It is guaranteed to work for any array with the following properties: 
    1. Each element in the array A is between 0 and N−1 inclusive (0≤A[i]≤N−1) 
    2. No element is repeated 
    3. The array is size N (all elements from 0 to N - 1 show up exactly once)
"""

#source: Leetcode
