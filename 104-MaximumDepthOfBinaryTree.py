# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        stack = [(1, root)]
        result = 0
        while stack:
            depth, node = stack.pop()
            if node:
                result = max(result, depth)
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
        return result
 
#BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        level = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
        return level
    
    
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([(root, 1)])
        res = 1
        while queue:
            node, level = queue.popleft()
            res = max(res, level)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res
