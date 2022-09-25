class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif curSum > 0: k -= 1
                else: j += 1
                
        return res
