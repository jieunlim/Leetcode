# O(n) / O(n)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursive(pnode, qnode):
            if not pnode and not qnode: return True
            if pnode and qnode: 
                if pnode.val != qnode.val: 
                    return False
                return recursive(pnode.left, qnode.left) and recursive(pnode.right, qnode.right)
            else:
                return False
        return recursive(p, q)
