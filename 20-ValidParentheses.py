#T: O(N), S: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'[':']', '(':')', '{':'}'}
        stack = []
        
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif stack:
                o = stack.pop()
                if ch == dic[o]:
                    continue
                else: return False
            else: return False
        return stack == []
