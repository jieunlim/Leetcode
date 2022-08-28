#T:O(n), S: O(n) - recursive stack when skewed binary tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return
        if root.val == p.val or root.val == q.val: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        else: return left or right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r or (root in [p, q]) : return root
        else: return l or r
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 
        
        def dfs(node):
            if not node: return
           # if node.val == p.val or node.val == q.val: return node 

                
            l = dfs(node.left)
            r = dfs(node.right)
            
            if l and r or (node in [p, q]) : return node
            else: return l or r
        
        return dfs(root)
