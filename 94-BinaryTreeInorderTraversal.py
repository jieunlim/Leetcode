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
