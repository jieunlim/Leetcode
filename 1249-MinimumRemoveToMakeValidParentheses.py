# T: O(n), S: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        sol = ''
        
        s = list(s)
        for i, ch in enumerate(s):
            if ch == "(": stack.append(i)
            elif ch ==')': 
                if stack: stack.pop()
                else: s[i]=''
        
        while stack:
            s[stack.pop()]=''
        
                
        return ''.join(s)
