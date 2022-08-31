class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def dfs(node):
            if not node: return float('inf'), float('-inf'), 0 #min, max, n
            lmin, lmax, lnum = dfs(node.left)
            rmin, rmax, rnum = dfs(node.right)
            n = float('-inf')
            
            if node.val > lmax and node.val < rmin:
                n = lnum + rnum + 1
                self.res = max(n, self.res)
            return min(node.val, lmin), max(node.val, rmax), n
        
            
        
        dfs(root)
        return self.res
