class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        n = len(ribbons)
        
        if sum(ribbons)<k: return 0
        
        start = 1
        end = max(ribbons)
        
        while start <= end:
            m = (start + end)//2
            res = 0
            
            for i in ribbons:
                res += i // m
            
            if res >= k:
                start = m + 1
            else:
                end = m -1
                
        return end
                
