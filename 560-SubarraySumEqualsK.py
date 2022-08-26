from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = res = 0
        dic = defaultdict(int)
        dic[0] = 1
        
        for n in nums:
            sum += n
            if sum - k in dic:
                res += dic[sum-k]
               
            dic[sum] += 1
            print(f"res={res}, dic={dic}")
        return res
