class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) //2
            need = 1
            cur = 0
            
            for w in weights:
                cur += w
                if cur > mid:
                    need += 1
                    cur = w
                
            if need > days:
                left = mid + 1
            else:
                right = mid
        return left
    
class Solution2:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights) 
        while l<r:
            m = (l + r)//2 
            need = 1
            capa = 0
            for w in weights:
                capa += w
                if capa > m:
                    need += 1
                    capa = w
            if need > days: 
                l = m+1
            else: #need <= days: r = m
                r = m
        return r
