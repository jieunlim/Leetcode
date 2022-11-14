class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i]>=idx:
                idx = i
        return idx == 0

    
#Greedy T: O(n), S: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        for i in range(len(nums)):
            if i > idx:
                return False
            idx = max(idx, i + nums[i])
  
        return  True
