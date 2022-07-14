class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = {s}
        while True:
            sol = []
            for ele in level:
                if self.isValid(ele):
                    sol.append(ele)
            if sol:
                return sol
            
            new_sol = set()
            
            for ele in level:
                for i in range(len(ele)):
                    new_sol.add(ele[:i]+ele[i+1:])
            level = new_sol
            
    def isValid(self, s):
        count = 0
        for c in s:
            if c =="(":
                count += 1
            elif c == ")":
                count -=1
                if count < 0:
                    return False
        return count == 0
        
