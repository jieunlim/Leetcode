#T: O(n), S: O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur = 1
        prev = 0
        sol = 0
        
        for i in range(1, len(s)):
            if s[i-1] != s[i]: 
                sol += min(prev, cur)
                print(f"sol: {sol}, prev:{prev}, cur:{cur}")
                prev, cur = cur, 1
            else: 
                cur += 1                

        return sol + min(prev, cur)
            
