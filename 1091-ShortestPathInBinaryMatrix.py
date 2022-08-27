
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
        res = float(inf)
        
        if grid[0][0]==1: return -1
        queue = deque([(0,0,1)]) #r, c, length
        
        while queue:
            r, c, length = queue.popleft()
            if r == n-1 and c == n-1: 
                return length
            

            for x,y in dirs:
                nr = x+r
                nc = y+c
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr,nc, length + 1))
                    
        
                
        return -1

class Solution2:
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
    
    
class Solution3:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1:
            return -1

        q = [(0, 0, 1)]
        while len(q) > 0:
            x, y, d = q.pop(0)
            if x == rows-1 and y == cols-1:
                return d
            for a, b in ((x-1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x+1, y-1)):
                if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 0:
                    grid[a][b] = 1
                    q.append((a, b, d+1))

        return -1
    
    
class Solution4:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)-1
        cols = len(grid[0])-1
        
        if grid[0][0] or grid[rows][cols]:
            return -1
        
        dir = [(-1,-1),(-1,0),(0,-1),(1,1),(1,0),(0,1),(1,-1),(-1,1)]
        q = deque()
        q.append([0,0])
        
        cnt = 0
        
        while q:
            cnt+=1
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                if r == rows and c == cols: return cnt
                for row, col in dir:
                    new_row, new_col = r+row, c+col
                    if 0<=new_row<=rows and 0<=new_col<=cols and grid[new_row][new_col]==0:
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 1
                
        return -1
    

