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
    
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        def helper(i, prev):
            if i == len(nums): return
            res.append(prev)
            for j in range(i+1, len(nums)):
                helper(j, prev + [nums[j]])
        
        for i in range(len(nums)):
            helper(i, [nums[i]])
        return res
    
    
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                backtrack(i+1, path + [nums[i]])
        
        backtrack(0,[])
        return res
    
class Solution4:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res += [cur + [num] for cur in res]
        
        return res
