# S, T: O(n) for counter + O(nlogk) for build heap

from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        res = []
        for key, val in cnt.items():
            heappush(heap, (val, key))
            if len(heap)>k:
                heappop(heap)
        
        
        for _ in range(k):
            res.append(heappop(heap)[1])
            
        return res


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
    
# O(n) for counter + O(nlogn) for build heap
#S: O(n)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapify(max_heap)
        print(max_heap)
        for i in range(k):
            res.append(heappop(max_heap)[1])
        return res
    
from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        res = []
        for key, val in cnt.items():
            heappush(heap, (-val, key))
        
        
        for _ in range(k):
            res.append(heappop(heap)[1])
            
        return res
