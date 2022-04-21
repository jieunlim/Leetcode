#T: O(n^2) S: O(1)
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        sol = 0
        
        for i in range(n):
            maxx = nums[i]
            minn = nums[i]
        
            for j in range(i, n):
                minn = min(minn, nums[j])
                maxx = max(maxx, nums[j])
                sol += maxx - minn
        return sol
