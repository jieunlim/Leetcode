from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        dir =[(0,1), (0,-1), (1,0), (-1,0)]
        
        queue = [(0,0,0,0)]
        visited = set((0,0,0))
        
        for r, c, obstaclecnt, stepcnt in queue:
            if r+1 == m and c+1 == n: return stepcnt
            for x, y in dir:
                nr, nc = r + x, c + y
                if 0 <= nr < m and 0 <= nc < n :
                    if grid[nr][nc]: #blocked
                        if obstaclecnt < k and (nr, nc, obstaclecnt+1) not in visited:
                            visited.add((nr, nc, obstaclecnt+1))
                            queue.append((nr,nc,obstaclecnt+1, stepcnt+1))
                    else: #not blocked
                        if (nr,nc,obstaclecnt) not in visited:
                            visited.add((nr,nc,obstaclecnt))
                            queue.append((nr,nc,obstaclecnt, stepcnt+1))
        return -1 #not possible
