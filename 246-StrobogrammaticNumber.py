class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        num = str(num)
        dic = {'8': '8', '1': '1', '0':'0', '6': '9', '9': '6'}
        
        l, r = 0, len(num)-1
        
        while l<r:
            if num[l] not in dic: return False
            elif dic[num[l]] == num[r]:
                l+=1
                r-=1
            else: return False
        if l == r:
            if num[l] in '810': return True
            else: return False
        return True

class Solution2:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num)-1
        num = str(num)
        same = ['8','1','0']
        diff = ['6','9']
        
        if len(num)==1:
            if num in same: return True
            else: return False
        
        
        while l<r:
         
            if num[l] in same and num[r] in same and num[l]== num[r]:
                l+=1
                r-=1
            elif (num[l] in diff) and (num[r] in diff) and (num[l] != num[r]):
                l+=1
                r-=1
            else:
                return False
        
        if len(num)%2 != 0:
            print(num[l] not in same)
            if num[l] in same: return True
            else: return False
        return True
                
        
