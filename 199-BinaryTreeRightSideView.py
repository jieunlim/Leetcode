# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        sol = []
        queue = [(root,0)]
        dic = defaultdict(list)
        
        while queue:
            node, level = queue.pop(0)
            dic[level].append(node.val)
            
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        for key, val in dic.items():
            sol.append(val[-1])
        return sol
        
        

class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        level = [root]
        sol = [root.val]
        while level:
            cur = []
            for node in level:
                if node.left: cur.append(node.left)
                if node.right: cur.append(node.right)
            if cur: sol.append(cur[-1].val)
            level = cur
        return sol
    
 class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        def helper(node, l):
            if not node: return
            if l == len(sol): sol.append(node.val)
            
            helper(node.right, l+1)
            helper(node.left, l+1)
        helper(root, 0)
        return sol
        
