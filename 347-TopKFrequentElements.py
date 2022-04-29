#T: O(nlogn), O(n + k)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k==len(nums): return nums
        m = Counter(nums)
        return heapq.nlargest(k, m.keys(), key=m.get)
 

#T: O(n), O(n)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for i in range(len(nums) + 1)]
        print(bucket)
        m = Counter(nums).items()
        
        for num, freq in m:
            bucket[freq].append(num)
            
        sol = []
        
        for sublist in bucket:
           
            for i in sublist:
                sol.append(i)
        return sol[::-1][:k]
