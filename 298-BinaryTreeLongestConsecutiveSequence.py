class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxVal = 0
        def helper(node, cnt):
            if not node: return 0
            self.maxVal = max(self.maxVal, cnt)
            if node.left:
                if node.val + 1 == node.left.val:
                    c = cnt + 1
                else:
                    c = 1
                helper(node.left, c)
            if node.right: 
                if node.val + 1 == node.right.val:
                    c = cnt + 1
                else:
                    c = 1
            
                helper(node.right, c)
        
        helper(root, 1)
        return self.maxVal

class Solution2:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxVal = 0
        def helper(node, cnt):
            if not node: return 0
            self.maxVal = max(cnt, self.maxVal)    
            if node.left:
                if node.val + 1 == node.left.val:
                    helper(node.left, cnt+1)
                else:
                    helper(node.left, 1)
                
            if node.right:
                if node.val + 1 == node.right.val:
                    helper(node.right, cnt+1)
                else: 
                    helper(node.right, 1)
           
        helper(root, 1)
        return self.maxVal
        
        
        
