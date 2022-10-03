#Deque, Time: O(N), Space: O(1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        res = []
        for i in range(len(nums)):
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i -k:
                dq.popleft()
            if i >= k-1:
                res.append(nums[dq[0]])
            
        return res
#Heap, Time: O(Nlogk), Space: O(n) for heap
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        heap,  res = [], []
        for i, val in enumerate(nums[:k]):
            heappush(heap, (-val, i))
        res = [-heap[0][0]]
        
        for i in range(k, len(nums)):
            while heap[0][1] <= i-k:
                heappop(heap)
            heappush(heap, (-nums[i], i))
            res.append(-heap[0][0])
        return res
                
# Time: O(N*K), Space: O(N-k+1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i:i + k]) for i in range(n - k + 1)]
                
