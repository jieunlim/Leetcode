# T: O(mn) S: O(mn)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set() #r, c
        q = deque([]) # r, c, step
        direction = [(-1,0), (1,0), (0, -1), (0, 1)] # up, down, left, right
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*': 
                    q.append((i, j, 0))
                    break
            if q: break
        while q:
            r, c, step = q.popleft()
            if grid[r][c] == 'X': continue
            if grid[r][c] == '#': return step
            for x, y in direction:
                nr, nc = r+x, c+y
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]!='X' and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc, step+1))
                    
        return -1
      
      
#W/O seen, change visited cell to 'X'

class Solution2:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque([]) # r, c, step
        direction = [(-1,0), (1,0), (0, -1), (0, 1)] # up, down, left, right
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*': 
                    q.append((i, j, 0))
                    break
            if q: break
        while q:
            r, c, step = q.popleft()
            if grid[r][c] == 'X': continue
            if grid[r][c] == '#': return step
            grid[r][c] = 'X'
            for x, y in direction:
                nr, nc = r+x, c+y
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]!='X':
                   
                    q.append((nr, nc, step+1))
                    
        return -1
