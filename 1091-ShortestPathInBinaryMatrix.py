
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)-1
        cols = len(grid[0])-1
        
        if grid[0][0] or grid[rows][cols]:
            return -1
        
        dir = [(-1,-1),(-1,0),(0,-1),(1,1),(1,0),(0,1),(1,-1),(-1,1)]
        q = [(0,0,1)]
        
        def helper(r, c, path):
            if r<0 or c<0 or r>rows or c>cols or grid[r][c]==1: return
            grid[r][c] = 1
            
            for new_r, new_c in dir:
                q.append((r + new_r, c+ new_c, path+1))
            
        print(q)
        for r, c, path in q:
            if r == rows and c == cols:
                return path
            else: helper(r, c, path)
                
        return -1
