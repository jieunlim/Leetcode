


#Min heap: T: O(Nlogk), S: O(k) for heap
    
 """
        loop through nums
        kth largest -> min heap with size k
        
        h[0] -> first element
"""

from heapq import heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        
        return heap[0]


      
      
# Max heap: O(nlogn)

from heapq import  heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num * -1)
            
        res = 0
        for _ in range(1, k):
            heappop(heap)
        
        return heap[0]*-1

