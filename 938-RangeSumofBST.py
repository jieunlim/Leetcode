from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Build a tree to run
    def buildTree(self, arr):

        if not arr: return
        root = TreeNode(arr[0])
        dQ = deque()
        dQ.append(root)

        i = 1
        while dQ:
            node = dQ.popleft()
            if i < len(arr):
                if arr[i] is not None and node: #for dealing '0' valus
                    node.left = TreeNode(arr[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i+=1
            if i < len(arr):
                if arr[i] is not None and node:
                    node.right = TreeNode(arr[i])
                    dQ.append(node.right)
                else:
                    dQ.append(None)
            i+=1
        #self.inOrderT(root)    
        return root

    def inOrderT(self, root):
        if root:
            self.inOrderT(root.left)
            print(root.val)
            self.inOrderT(root.right)

    #DFS-recursion
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        if not root:
            return total
            
        def helper(root):
            if not root: return
            if low <= root.val <= high:
                self.total += root.val
            
            if root.val > low:
                helper(root.left)
            if root.val <high:
                helper(root.right)
        helper(root)
        return self.total

obj = Solution()
arr = [ 5, 1, 6]
arr = [10, 5, 15, 3, 7, None, 18]
root = obj.buildTree(arr)
obj.inOrderT(root)

r = obj.rangeSumBST(root, 7, 15)
print(f"rtn : {self.total}")
