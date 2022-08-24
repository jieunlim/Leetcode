#T: O(nm), S: O(mn) - maintain Queue
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        direction = [(0,1), (0,-1), (-1,0), (1,0)] # right, left, up, down
        seen = set() #r, c
        q = deque([])#r, c, distance
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    seen.add((i, j))
                    q.append((i, j))  
        
        
        while q:
            r, c = q.popleft()
           
            for x, y in direction:
                nr, nc = x+r, y+c
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    mat[nr][nc] = mat[r][c] + 1
                    seen.add((nr, nc))
                    q.append((nr, nc))
        return mat
        
        

class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque([])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    mat[r][c] = -1
                else: 
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()
            
            for x, y in dirs:
                nr = x + r
                nc = y + c
                
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
                    
        return mat
