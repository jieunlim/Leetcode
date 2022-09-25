#T: O(nm), S: O(1)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        res = 0
        
        def dfs(r, c):
            if 0 <= r < n and 0 <= c < m and grid[r][c] == "1":
                grid[r][c] = '0'
                
                for x, y in dirs:
                    nr = r + x
                    nc = c + y
                    
                    dfs(nr, nc)
                
        for r in range(n):
            for c in range(m):
                if grid[r][c]=='1':
                    dfs(r, c)
                    res += 1
                    
        return res
    
    

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
      
class Solutio2:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        T: O(N*M), S: O(1)
        DFS
        """
        
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        cnt = 0
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            
            grid[r][c] = '0'
            
            for x, y in dirs:
                new_r = r + x
                new_c = c + y

                dfs(new_r, new_c)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    cnt += 1
                    
        return cnt
                
