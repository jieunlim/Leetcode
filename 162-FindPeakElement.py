class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        if len(nums)==2: return 0 if nums[0]>nums[1] else 1
        l,r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            
            if nums[m-1] < nums[m] and nums[m+1] < nums[m]: return m
            elif nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m-1
        return l 
