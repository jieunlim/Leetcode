#Solution 1 Recursive: O(n) / O(h)
class Solution1:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.total = 0
        
        def dfs(node, subsum):
            cur = subsum * 10 + node.val 
            
            if not node.left and not node.right:
                self.total += cur
            
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
                
        dfs(root, 0)
        return self.total
      
#Solution 2 Iterative: O(n) / O(h) 
class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.total = 0
        
        stack = [(root, 0)]
        while stack:
            node, cur = stack.pop()
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                self.total += cur
            if node.left:
                stack.append((node.left, cur))
            if node.right:
                stack.append((node.right, cur))
            
                
        
        return self.total
