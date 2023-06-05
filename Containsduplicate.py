class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: #input array
    
    hashset = set() #define hashset (like an empty dictionary where we add the numbers in array as we iterate through it
    
    for n in nums: #iterate one by one through array
      if n in hashset:  #duplicate 
        return True
      hashset.append(n)
    return False 
