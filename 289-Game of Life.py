class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def getCnt(i, j):
            cntOne = 0
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1)]:
                if x >= 0 and x < rows and y >= 0 and y < cols and board[x][y] in [1,2] :
                    cntOne += 1
            return cntOne
        
        def helper(i, j):            
            cntOne = getCnt(i, j)

            if board[i][j] == 1:
                if cntOne < 2 or cntOne > 3:
                    board[i][j] = 2
                # elif cntOne == 2 or cntOne == 3:
                #     board[i][j] = 1
            else:
                if cntOne == 3:
                    board[i][j] = -1
                    
        if not board: return None
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                helper(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0