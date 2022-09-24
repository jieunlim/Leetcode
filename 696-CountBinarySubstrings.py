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
            

# T: O(N), S: O(N)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        arr = []
        cnt = 1
        s += " "
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                cnt+=1
            else:
                arr.append(cnt)
                cnt = 1
        print(arr)
        for i in range(len(arr)-1):
            res += min(arr[i], arr[i+1])
        
        return res
