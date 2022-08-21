class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minheap = []
        res = []
        for n in arr:
            minheap.append((abs(n-x), n))
        heapify(minheap)
        for i in range(k):
            res.append(heappop(minheap)[1])
        return sorted(res)
                           
