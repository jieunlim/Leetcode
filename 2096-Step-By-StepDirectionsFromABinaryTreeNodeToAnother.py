##Solution 1: O(n) / O(n)
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node):
            if not node: return
            if node.val == startValue or node.val == destValue: return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right: return node
            else: return left or right
        root = lca(root)
        startPath, destPath = "", ""
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node.val == startValue: startPath = path
            if node.val == destValue: destPath = path
            if node.left : stack.append((node.left, path + 'L'))
            if node.right : stack.append((node.right, path+'R'))
        return 'U' * len(startPath) + destPath
