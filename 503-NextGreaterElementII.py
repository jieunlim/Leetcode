# T/S : O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        sol = [-1]*len(nums) 
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                sol[stack.pop()] = nums[i]
            stack.append(i)
            
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                sol[stack.pop()] = nums[i]
            if not stack:
                break
            
        return sol
