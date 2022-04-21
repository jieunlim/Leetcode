#T: O(nm), S: O(1)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        r = len(grid)
        c = len(grid[0])
        
        def dfs(i, j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j] != "1":
                return
            grid[i][j] = '*'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range (r):
            for j in range (c):
                if grid[i][j]=='1': 
                    res +=1
                    dfs(i, j)
        return res
        
#T: O(nm), S: O(1)
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        r = len(grid)
        c = len(grid[0])
        
        def dfs(i, j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j] != "1":
                return
            grid[i][j] = '*'
            for x, y in [[1,0],[-1,0],[0,1],[0,-1]]:
                dfs(i+x, j+y)

        for i in range (r):
            for j in range (c):
                if grid[i][j]=='1': 
                    res +=1
                    dfs(i, j)
        return res 
        
#BFS T: O(nm), S: O(1)
from collections import deque
class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        if not grid or not grid[0]: return res
        
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    res += 1
        return res
    
    

    def bfs(self, grid, i, j):
        queue = deque()
        queue.append((i, j))
        grid[i][j] = '*'
        
        while queue:
            direction = [(0,1), (0, -1), (-1, 0), (1, 0)]
            i, j = queue.popleft()
            for x, y in direction:
                nr, nc = i + x, j + y

                if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc] != "1":
                    continue

                queue.append((nr, nc))
                grid[nr][nc] = '*'  
