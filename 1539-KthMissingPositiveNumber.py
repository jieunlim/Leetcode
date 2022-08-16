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
