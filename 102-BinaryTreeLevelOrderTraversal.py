# 103, 958, 222
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        res = []
        node = root
        
        while queue:
            cur = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)      
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(cur)
        return res
            
