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

#T: O(nlogn) S: n!
import heapq

class Solution2:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        sol = 0
        
        for i in range(n):#n
            maxx = [-nums[i]] #max heap
            minn = [nums[i]] #min heap
        
            for j in range(i, n): #log(n)
                heapq.heappush(maxx, -nums[j])
                heapq.heappush(minn, nums[j])
                sol += -maxx[0] - minn[0]
        return sol
