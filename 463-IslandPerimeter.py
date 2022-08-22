class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        sol = 0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    sol += 4
                    for x, y in dir:
                        if 0<=r+x<n and 0<=c+y<m and grid[r+x][c+y] == 1:
                            sol -= 1
        return sol
