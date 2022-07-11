#O(n), O(1) - no consider recursion stack
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.mindiff = float(inf)
        
        self.sol = None
        
        def helper(node):
            
            if not node: return        
            if abs(target - node.val) < self.mindiff:
                self.sol = node.val
                self.mindiff = abs(target - node.val)
        
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.sol
      
 #O(h), O(1)
class Solution2:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        sol = root.val
        while root:
            if abs(root.val - target) < abs(sol - target):
                sol = root.val
            if target == root.val: return root.val
            elif target < root.val: root = root.left
            else: root = root.right
        return sol
