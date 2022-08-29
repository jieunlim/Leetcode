#T, S: O(f+s)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        if not firstList or not secondList: return res
        
        while i < len(firstList) and j < len(secondList):
            
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            
            if s1 > e2: j += 1
            elif s2 > e1: i += 1
            else: 
            
                start = max(s1, s2)
                end = min(e1, e2)
            
                res.append([start, end])
                
                if e2 > e1: i += 1
                else: j += 1
                    
        return res
        
    
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    
        sol = []
        if not firstList or not secondList: return sol
        
        f,s = 0, 0
        
        while f < len(firstList) and s < len(secondList):
           
            if firstList[f][0] > secondList[s][1]: s +=1 
            elif secondList[s][0] > firstList[f][1]: f += 1
            else:
                a = max(secondList[s][0], firstList[f][0])
                b = min(secondList[s][1], firstList[f][1])
                sol.append([a, b])
               
                if secondList[s][1] > firstList[f][1]:
                    f+=1
                else:
                    s+=1
         
        return sol
