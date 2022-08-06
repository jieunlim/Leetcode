class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {}
        dic[0] = -1
        subsum = 0
        
        for i in range(len(nums)):
            subsum += nums[i]
            if subsum % k not in dic:
                dic[subsum%k] = i
            else:
                if i-dic[subsum%k]>1:
                    return True
            
        return False
