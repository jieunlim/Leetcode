#T: O(n), S: O(1) 
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        
        i = j = 0
        
        while i<len(encoded1) and j<len(encoded2):
            v1, c1 = encoded1[i]
            v2, c2 = encoded2[j]
            
            p = v1 * v2
            cnt = min(c1, c2)
            
            encoded1[i][1] -= cnt
            encoded2[j][1] -= cnt
                
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
            
            if not res or res[-1][0] != p:
                res.append([p, cnt])
            else: res[-1][1] += cnt
                
            
            
        return res
    
#TLE
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        l1, l2 = [], []
        res = []
        for num, cnt in encoded1: 
            for _ in range(cnt):
                l1.append(num)
        for num, cnt in encoded2: 
            for _ in range(cnt):
                l2.append(num)
        
        cur = []
        for a, b in zip(l1, l2):
                cur.append(a * b)
        
        cnt = 0
        res.append([cur[0], 0])
        for i in range(len(cur)):
            if cur[i] == res[-1][0]:
                res[-1][1]+=1
            else:
                res.append([cur[i], 1])
        return res
        
