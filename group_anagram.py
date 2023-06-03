from collections import defaultdict  #library that assigns keys to the dictionary



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
      anagram_map = defaultdict(list) 
      result = []   #saves output 
      
      strs = ["eat","tea","tan","ate","nat","bat"] #input 
    
      for s in strs:
        sorted_s = tuple(sorted(s)) #tuple is mutable 
         anagram_map[sorted_s].append(s) #append strs to anagram_map 
  #print(anagram_map) 
        for value in anagram_map.values(): #assign values to keys 
            result.append(value)
            
       return result 
        
