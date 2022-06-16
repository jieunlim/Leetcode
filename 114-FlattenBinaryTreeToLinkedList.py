# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        if not root.left and not root.right: return root
        
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        
        if l:
            l.right = root.right
            root.right = root.left
            root.left = None
        
       # We need to return the "rightmost" node after we are
       # done wiring the new connections.
        return r if r else l
      

class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        
        node = root
        while node:
            if node.left:
                
                rightmost = node.left
                
                 # Find the rightmost node
                while rightmost.right: 
                    rightmost = rightmost.right
                
                 # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
                
             # move on to the right side of the tree
            node = node.right
            
