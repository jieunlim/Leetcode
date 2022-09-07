#O(n)/O(n)

Iterative
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return
        
        def is_same(n1, n2):
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            return is_same(n1.left, n2.left) and is_same(n1.right, n2.right)
        
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if is_same(node, subRoot): return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False
    
Recursive

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
