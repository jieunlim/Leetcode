# T: O(n), S: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        sol = []
        dic = defaultdict(list) #{0: [3,15], -1: [9], 1: [7]}
        dic[0].append(root.val)
        mincol = 0
        queue = deque()
        queue.append([root, 0])
        while queue:
            
            node, col = queue.popleft()
            level = []
            if node.left:
                queue.append([node.left, col-1])
                dic[col-1].append(node.left.val)
                mincol = min(mincol, col -1)
            if node.right:
                queue.append([node.right, col+1])
                dic[col+1].append(node.right.val)
        
        for i in range(mincol, mincol + len(dic)):
            sol.append(dic[i])
        return sol
