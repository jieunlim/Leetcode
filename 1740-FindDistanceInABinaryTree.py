# T: O(n), S: O(n)

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q: return 0
        def dfs(node):
            if not node: return 
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            
            if l and r or node.val in [p, q]: return node
            else: return l or r
            
        
        def dist(node, target):
            if not node: return float('inf')
            if node.val == target: return 0
            return 1 + min(dist(node.left, target), dist(node.right, target))
        
        lca = dfs(root)
        return dist(lca, p) + dist(lca, q)
            
        
