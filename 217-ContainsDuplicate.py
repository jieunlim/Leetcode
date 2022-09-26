#T, S: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen: return True
            seen.add(num)
        return False
    
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
 
#T:O(Nlogn), S: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        curr = nums[0]
        
        for num in nums[1:]:
            if num ^ curr == 0: return True
            else: curr =num
        return False
