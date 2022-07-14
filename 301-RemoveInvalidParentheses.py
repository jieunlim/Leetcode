class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        sol = []
        cur = set()
        cur.add(s) 
        
        while cur:
            for e in cur:
                if self.isValid(e):
                    sol.append(e)
            if sol: return sol


            new_cur = set()
            for e in cur:
                for i in range(len(e)):
                    new_cur.add(e[:i]+e[i+1:])
            cur = new_cur

        
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch not in ['(',')']:
                continue
            elif ch == '(':
                stack.append(ch)
            elif stack and ch == ')':
                stack.pop()
            else: return False
        return stack == []
    
            
