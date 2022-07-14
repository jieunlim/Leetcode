class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        stack = 0
        for e in s:
            if e == '[':
                stack += 1
            elif stack and e==']':
                stack -= 1
            else:
                res += 1
                stack += 1
        return res
