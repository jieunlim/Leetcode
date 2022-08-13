# time complexity O(max(N1, N2))
# space complexity O(max(N1, N2))

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1)-1, len(num2)-1
        res = ""
        carry = 0
        
        while i>=0 or j>=0 or carry:

            
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            
            total = n1 + n2 + carry
            carry = total //10
            
            res = str(total%10) + res
            
            i-=1
            j-=1
        
        return res
            
