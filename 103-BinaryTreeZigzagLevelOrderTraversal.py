# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    
    # My Solution:  
    #   Similar to regular BFS using queue, 
    #   but traverse level by level.
    #   At each level, switch direction of adding nodes to 
    #   level_res.  
        if not root: return []
        queue = deque([])
        queue.append((root, 1))
        res = []
        while queue:
            level = []
            direction = 1
            for _ in range(len(queue)):
                node, direction = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append((node.left, direction * -1))
                if node.right:
                    queue.append((node.right, direction * -1))
                
            if direction == -1: 
                level = level[::-1]
            res.append(level)
            
        return res
            
