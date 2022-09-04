# S, T: O(n)
Tip: (ord('b') + ord('a')) % 26 + ord('a')
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans, shift = "", 0
        for i in range(len(shifts)-1, -1, -1):
            ans += chr((ord(s[i]) + shift + shifts[i] - ord('a'))% 26 + ord('a'))
            shift += shifts[i]
        return ans[::-1]

#TLE
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = list(s)
        for i in range(len(s)):
            for j in range(i+1):
                ch = (ord(res[j]) + shifts[i] - ord('a'))% 26 + ord('a')
                res[j] = chr(ch)
                
        return ''.join(res)
      
