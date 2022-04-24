#TLE - T: O(m * n) m: # of data, n: #or 1, S: O(1)
class Solution1:
    def minSwaps(self, data: List[int]) -> int:
        n = sum(data)
        sol = len(data)
        
        
        
        for i in range(len(data)-n+1):
            temp = 0
            temp = n - sum(data[i:i+n])
            sol = min(temp, sol)
        return sol
      
# T: O(n), S: O(1)
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = sum(data)
        ans = len(data)
        cnt_one = max_one = 0
        left = right = 0
        
        while right < len(data):
            cnt_one += data[right]
            right += 1
            
            if right - left > n:
                cnt_one -= data[left]
                left += 1
            max_one = max(max_one, cnt_one)
        return n - max_one
        
