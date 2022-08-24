class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        
        while l <= r:
            
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
                
            m = l + (r - l)//2
            if target == nums[m]: return True
                
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return False
        
