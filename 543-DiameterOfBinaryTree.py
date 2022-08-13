class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = 0
        def helper(node):
            nonlocal d
            
            if not node: return 0
            
            l = helper(node.left)
            r = helper(node.right)
            
            d = max(d, l + r)
            
            return max(l, r) + 1
    
        helper(root)
        return d
