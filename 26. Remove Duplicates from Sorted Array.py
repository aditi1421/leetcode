class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: #take input 
     l = 1 #left pointer 
    #r = right pointer
    for r in range(1,len(nums)):  #right pointer iterates through nums
      if nums[r] != nums[r-1]: #if right pointer is not equal to the pointer besides it
        nums[l] = nums[r] # append l = r, we need to increase the number 
      l += 1
    return l  #return l, number of no duplicates 
        
