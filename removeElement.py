class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)): #iterating through array with pointer i 
        #pushing non vals to the beginning
            if nums[i] != val: #if we see a number that is not the value then swap
                #partition 
                nums[k] = nums[i] 
                k += 1
        return k #skip special values 
