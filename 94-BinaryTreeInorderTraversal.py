#recursively
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        sol = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            sol.append(node.val)
            dfs(node.right)
        dfs(root)
        return sol
    
#iteration
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
