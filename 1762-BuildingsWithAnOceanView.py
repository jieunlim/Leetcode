#T: O(n), S: O(n)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        sol = [len(heights)-1]
        
        for i in range(len(heights)-2, -1, -1):
            if heights[i]>heights[sol[-1]]: sol.append(i) 
        
        return sol[::-1]
