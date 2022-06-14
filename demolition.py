
'''
"""
Demolition Robot
Given a matrix with values 0 (trenches) , 1 (flat) , and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). If not possible then return -1.
The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
The demolition robot cannot enter 0 trenches and cannot leave the matrix.
Sample Input :
[1, 0, 0],
[1, 0, 0],
[1, 9, 1]]
Sample Output :
3

"""




'''


from collections import deque

def demolition(matrix):
    m, n = len(matrix), len(matrix[0])
    if m <1 or n<1: return -1
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque([(0,0)])
    visited = set([0,0])
    dist = -1
    
    
    while queue:
        dist+=1
        size = len(queue)
        
        for _ in range(size):
            i, j = queue.popleft()
            if matrix[i][j] == 9:
                return dist
            
            for x, y in dir:
                nx,ny = i+x, j+y
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny]!=0 and (nx,ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return -1

from collections import deque
def demolition2(matrix):
    m, n = len(matrix), len(matrix[0])    
    direction = [(1,0), (-1,0), (0,1),(0,-1)]
    q = deque([])
    q.append((0, 0, 0)) # r, c, step
    seen = set()
    
    while q:
        r, c, step = q.popleft()
        if matrix[r][c] == 9: return step
        if matrix[r][c] == 1:
            for x, y in direction:
                nr, nc = r+x, c+y
                if 0<=nr<m and 0<=nc<n and (nr, nc, step+1) not in seen:
                    seen.add((nr, nc, step+1))
                    q.append((nr, nc, step+1))
    

    return -1





matrix = [
[1, 0, 0],
[1, 0, 0],
[1, 9, 1]
]

print(demolition(matrix))
