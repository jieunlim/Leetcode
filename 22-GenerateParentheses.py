#T: 2^2n, S: O(n) for storing sequence(path)
# about n, the options could be binary tree, the tree could be 2n level.
# The number of node would be 2^2n

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(l, r, path):
            
            if len(path) == 2*n: 
                res.append(path)
                return
            if l < n:
                backtrack(l+1, r, path + '(')
            if l > r: 
                backtrack(l, r+1, path + ')')
        
        
        res = []
        backtrack(0, 0, '')
        return res
