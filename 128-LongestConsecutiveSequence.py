#Time: O(n), Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        max_cnt = 0
        
        for nums in s:
            if nums -1 in s:
                continue
            j = 1
            while nums + j in s: 
                j += 1
            max_cnt = max(max_cnt, j)
            
        return max_cnt
