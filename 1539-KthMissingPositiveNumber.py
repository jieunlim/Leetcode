# O(log n) / O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        
        while l <= r:
            m = l + (r - l)//2
            missing = arr[m] - m - 1
            if missing < k:
                l = m + 1
            else:
                r = m - 1
                
                
        return arr[r] + (k - (arr[r] - r - 1)) # k + r - 1
            
# O(n) / O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        idx = 1
        missing_list = []
        
        for i, num in enumerate(arr):
            while idx < num:
                missing_list.append(idx)
                if len(missing_list) == k: return missing_list[-1]
                idx += 1
            else: 
                idx += 1
        return k- len(missing_list) + arr[-1]
