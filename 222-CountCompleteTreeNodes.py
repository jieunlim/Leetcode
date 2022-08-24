class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            res += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
