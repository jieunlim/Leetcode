class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target - num]]
            else:
                dic[num] = i
                

class Solution:
    def twoSum(self, nums, target) :
        
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                if nums [j] == target - nums[i]:
                    return [i, j]
obj = Solution()
nums = [2,7,11,15]
target = 9
print(obj.twoSum(nums, target))
print("hello")
