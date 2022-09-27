#Quick Select, T: avg-O(n), S: O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #k번째로 큰거 : len(nums) - k 번째로 작은거
        k= len(nums) - k
        
        def findKthSmallest(l, r):
            pivot = partition(l, r)
            if k < pivot:
                return findKthSmallest(l, pivot-1)
            if k > pivot:
                return findKthSmallest(pivot + 1, r)
            return nums[k]
        
        
        #rightmost: pivot
        def partition(l, r):
            p = l
            while l < r:
                if nums[l] < nums[r]:
                    nums[l], nums[p] = nums[p], nums[l]
                    p += 1
                l += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p
        
    
        return findKthSmallest(0, len(nums)-1)

    
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition (nums, start, end): #Decreasing order
            pivot = start
            while start < end:
                while start < end and nums[end] <= nums[pivot]:
                    end-=1
                while start < end and nums[pivot] <= nums[start]:
                    start += 1
          
                nums[start], nums[end] = nums[end], nums[start]
            nums[end], nums[pivot] = nums[pivot], nums[end]
            return end
        
        def quicksort(nums, start, end):
            p = partition(nums, start, end)
            
            if p == k-1:
                return nums[p]
            elif p < k-1:
                return quicksort(nums, p+1, end)
            else:
                return quicksort(nums, start, p-1)
        return quicksort(nums, 0, len(nums)-1)
    
    
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

