class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
   
        output = [[]]
        
        for num in nums:  
            r = []
            for curr in output:
                r += [curr + [num]]
            output += r
                #output += [curr + [num]]
                
        return output
    
    
    
