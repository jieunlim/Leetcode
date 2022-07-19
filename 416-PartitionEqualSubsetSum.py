class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums, target, cache):
            if target < 0 or target in cache: return False
            if target == 0: return True
            cache.add(target)
            for i, n in enumerate(nums):
                if dfs(nums[i+1:], target-n, cache): return True
            return False
        
        
        target, remaining = divmod(sum(nums), 2)
      
        if remaining != 0: return False
        return dfs(nums, target, set())
        
