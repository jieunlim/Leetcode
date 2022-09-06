class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root: return False
        
        
        def sameTree(r, s):
            if not r and not s: return True
            if not s or not r: return False
            if r.val != s.val: return False
            return sameTree(r.left, s.left) and sameTree(r.right, s.right)
        
        

        if not root: return False
        if not subRoot: return True
        
        if root.val == subRoot.val and sameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root: return False
        
        
        def sameTree(r, s):
            if not r and not s: return True
            if s and not r: return False
            if r and not s: return False
            if r.val != s.val: return False
            return sameTree(r.left, s.left) and sameTree(r.right, s.right)
        
        
        def helper(r, s):
            if not r: return False
            if r.val == s.val and sameTree(r, s): return True
            return helper(r.left, s) or helper(r.right, s)
        
        return helper(root, subRoot)
