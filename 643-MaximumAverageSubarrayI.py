class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        
        res = s
        
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            res = max(res, s)
        
        return res/k
