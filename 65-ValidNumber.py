class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        metE, metDot, metDigit = False, False, False
        
        for i, ch in enumerate(s):
            
            if ch in '+-':
                if i > 0 and s[i-1]!='e': return False
            elif ch in 'Ee':
                if metE or not metDigit: return False
                metE = True
                metDigit = False
            elif ch == '.':
                if metDot or metE: return False
                metDot = True
            elif ch in '0123456789':
                metDigit = True
            else:
                return False
        
        return metDigit
