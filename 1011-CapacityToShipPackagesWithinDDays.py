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
