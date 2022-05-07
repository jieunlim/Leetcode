#T: O(n), S: O(#'(')
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        sol = 0
        stack = []
        for i in s:
            if i == '(': stack.append(i)
            elif i== ")" and stack and stack[-1] == "(": stack.pop()
            else: sol += 1
        return len(stack) + sol
      
      
#T: O(n), S: O(1)
 class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        opening = ans = 0
        
        for i in s:
            if i == '(': opening +=1
            elif i== ")": 
                if opening: 
                    opening -=1
                else: ans += 1
            
            
        return opening + ans
