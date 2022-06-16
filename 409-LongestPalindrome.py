class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for ch in s:
            if ch not in ss:
                ss.add(ch)
            else:
                ss.remove(ch)
        if len(ss)!= 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)
