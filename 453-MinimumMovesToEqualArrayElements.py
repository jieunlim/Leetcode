#T:O(n), S: O(1)
class Solution:
    def minMoves(self, nums: List[int]) -> int: 
        return sum(nums) - min(nums) * len(nums)
        

#T: O(nlogn) for sorting, S: O(1)
class Solution:
    def minMoves(self, nums: List[int]) -> int: 
        nums.sort()
        res = 0
        for i in range(len(nums)-1,-1,-1):
            res += nums[i] - nums[0]
        return res
