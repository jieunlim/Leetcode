class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s)==0 and len(t)==0: return False
        
        i = j = 0
        flag = False
        
        if len(s) + 1 == len(t): #insert
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    if flag: return False
                    j += 1
                    flag = True
                else:
                    i += 1
                    j += 1
                    
            return True
        
        elif len(s) == len(t): #replace or same
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    if flag: return False
                    flag = True
                
                i += 1
                j += 1
                
            return flag
            
        elif len(s) -1 == len(t): #delete
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    if flag: return False
                    i += 1
                    flag = True
                else:
                    i += 1
                    j += 1
            return True
