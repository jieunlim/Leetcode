#O(logn), binary search

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] - nums[0] - mid < k:  
                l = mid + 1
            else:
                r = mid - 1
        # return nums[0] + k + l
        
        return nums[r] + k - (nums[r] - nums[0] - r)  

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
  
