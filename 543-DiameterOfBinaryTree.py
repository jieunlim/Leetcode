#124, 1522
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = 0
        def helper(node):
            nonlocal d # or self.d
            
            if not node: return 0
            
            l = helper(node.left)
            r = helper(node.right)
            
            d = max(d, l + r)
            
            return max(l, r) + 1
    
        helper(root)
        return d
    
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        if not root: return 0
        
        def helper(node):
            if not node: return 0
            first = second = 0
            for n in (node.left, node.right):
                depth = helper(n)
                if depth > first:
                    first, second = depth, first
                elif depth > second:
                    second = depth
                    

            self.d = max(self.d, first + second)
            return first + 1
        
        helper(root)
        return self.d
