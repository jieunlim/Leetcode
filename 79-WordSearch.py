# Space O(1)
# Time O(n*m*L^3)
class Solution:
    def exist(self, board, word):
        r, c = len(board), len(board[0])
        
      
        def dfs(i, m, n):
            if i == len(word):
                return True
            if m < 0 or n < 0 or m >= r or n >= c or word[i] != board[m][n]:
                return False
            
            board[m][n] = '#'
            res = dfs(i+1, m+1, n) or dfs(i+1, m-1, n) or dfs(i+1, m, n+1) or dfs(i+1, m, n-1)
            board[m][n] = word[i]
            return res
        
        
        i = 0
        for m in range(r):
            for n in range(c):
                if board[m][n] == word[i]:
                    if dfs(i, m, n):
                        return True
                    
                     
        return False

board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"

obj = Solution()
print(obj.exist(board, word))