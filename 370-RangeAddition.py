#TLE

class Solution1:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*length
        
        for start, end, val in updates:
     
            for i in range(start, end+1):
                res[i] += val
                
        return res

# T: O(n+k) k: #of updates, S: O(1)
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*length
        
        for start, end, val in updates:
           
            res[start]+=val
            if end + 1 < length:
                res[end+1]-=val
        
        for i in range (1,length):
            res[i] +=res[i-1]            
                
        return res      
