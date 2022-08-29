# BFS
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        queue = deque([root])
        
        while queue:
            maxval = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                maxval = max(maxval, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(maxval)
        return res
    
    
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        queue = deque([root])
        
        while queue:
            curlevel = []
            maxval = float('-inf')
            for node in queue:
                maxval = max(maxval, node.val)
                if node.left:
                    curlevel.append(node.left)
                if node.right:
                    curlevel.append(node.right)
            queue = curlevel
            res.append(maxval)
        return res
# DFS

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        
        def helper(node, level):
            if not node: return
            if level == len(res): res.append(node.val)
            else: 
                res[level] = max(res[level], node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
       
        
        helper(root, 0)
        
        return res
                
