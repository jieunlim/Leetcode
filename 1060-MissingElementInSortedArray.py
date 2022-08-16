class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        cnt = []
        for i, n in enumerate(nums):
            cnt.append(n-nums[0]-i)
        
        if k > cnt[-1]:
            return nums[-1] + k - cnt[-1]
        
        for i, n in enumerate(cnt):
            if k <= n:
                break
            idx = i
            
        return nums[idx] + k - cnt[idx]
  
