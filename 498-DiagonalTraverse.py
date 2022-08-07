class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        result = []
        x, y = 0, 0
        
        for i in range(rows + cols-1):
            if i%2 == 0: # even: x starting row+col
                x = min(i, rows-1)
                y = i-x
                while x>=0 and y < cols:
                    result.append(mat[x][y])
                    x-=1
                    y+=1

            else: # odd: y starting row+col 
                y = min(i, cols-1)
                x = i-y
                
                while  y>=0 and x < rows:
                    result.append(mat[x][y])
                    x+=1
                    y-=1
            
        return result
