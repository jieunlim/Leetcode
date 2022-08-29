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
