class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = res = 0
        dic = {}
        
        for i, num in enumerate(nums):
            presum += num
            
            if presum == k: res = i + 1
            
            if presum - k in dic:
                res = max(res, i - dic[presum-k])
            
            if presum not in dic:
                dic[presum] = i
        return res
