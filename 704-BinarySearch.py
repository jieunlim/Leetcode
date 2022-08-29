class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = l + (r - l)//2
            if nums[m] <= target:
                l = m + 1
            else: r = m - 1
                
        return r if nums[r] == target else -1
      
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l)//2
            if nums[m] >= target:
                r = m
            else: l = m + 1
                
        return r if nums[r] == target else -1
