# S, T: O(r*c) 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        print(dp)
        
        for j in range(1, len(grid)):
           
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                dp[r][c] = min(dp[r-1][c] + grid[r][c], dp[r][c-1] + grid[r][c])
                
        return dp[-1][-1]

# T: O(r*c)  using input Grid : O(1) space     
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        for i in range(1, len(grid[0])):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        
        for i in range(1, len(grid)):
            grid[i][0] = grid[i-1][0] + grid[i][0]
            
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = min(grid[r-1][c], grid[r][c-1]) + grid[r][c]
        return grid[-1][-1]
