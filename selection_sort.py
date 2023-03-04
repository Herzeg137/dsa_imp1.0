nums = [64, 25, 12, 22, 11]

#traverse
for i in range(len(nums)):

  #find the minimum element
  min_ele = i
  for j in range(i+1, len(nums)): #A[i+1::]
    #compare
    
    if nums[min_ele] > nums[j]:
      min_ele = j

  #otherwise, swap them
  nums[i], nums[min_ele] = nums[min_ele], nums[i]

print(nums)
