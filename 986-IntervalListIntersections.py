#T, S: O(f+s)

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
