class Solution:
    def myAtoi(self, s: str) -> int:
                
        ans = ''
        s = s.strip()
        if not s: return 0
   
        negative = False
        
        if s[0] in "-+":
            if s[0]=='-': negative = True
            s = s[1:]
        
        for ch in s:
            if ch.isnumeric(): 
                ans += ch
            else: break
                
        if not ans: return 0
        
        if negative:
            if int(ans)*-1 < -pow(2, 31): return -pow(2,31)
            else: return int(ans)* -1
        elif not negative:
            if int(ans) > pow(2, 31)-1: 
                return pow(2,31)-1
            else: return int(ans)
            
