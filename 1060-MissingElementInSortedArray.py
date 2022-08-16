class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        misCnt = []
        for i, n in enumerate(nums):
            misCnt.append(nums[i] - nums[0] - i)
        
        if k > misCnt[-1]: return nums[-1] - misCnt[-1] + k
        
        missing, idx = 0, 0
        
        for i, cnt in enumerate(misCnt):
            if cnt >= k: break
            missing = cnt
            idx = i 
        return nums[idx] - misCnt[idx] + k
           
