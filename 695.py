class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        r = len(grid)
        c = len(grid[0])
        self.maxArea = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    self.maxArea = max(self.maxArea, self.findMax(grid, i, j, r, c))
        return self.maxArea
    
    def findMax(self, mat, i, j, r, c):
        if i>=0 and j>=0 and i<r and j<c and mat[i][j] == 1:
            mat[i][j] = 0
            return 1 + self.findMax(mat, i-1, j, r, c) + self.findMax(mat, i+1, j, r, c) + self.findMax(mat, i, j-1, r, c) + self.findMax(mat, i, j+1, r, c)
        return 0
    
    