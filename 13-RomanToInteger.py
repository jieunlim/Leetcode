class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        dic = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for i in range(len(s)-1, -1, -1):
            
            if s[i] == 'I' :
                if i + 1 < len(s) and s[i+1] in 'VX':
                    res -= 1
                    continue
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i+1] in 'LC':
                    res -= 10
                    continue
            elif s[i] == 'C':
                if i + 1 < len(s) and s[i+1] in 'DM':
                    res -= 100
                    continue
            
            res += dic[s[i]]
                
        return res
            
        
