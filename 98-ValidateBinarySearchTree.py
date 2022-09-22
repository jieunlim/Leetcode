#333. Largest BST Subtree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.isTrue = True
        
        def helper(node):
            if not node: return float('-inf'), float('inf') #max, min
            lmax, lmin = helper(node.left)
            rmax, rmin = helper(node.right)
            if not lmax < node.val< rmin:
                self.isTrue = False
            
            return max(node.val, rmax), min(node.val, lmin)
        
        helper(root)
        return self.isTrue
        
