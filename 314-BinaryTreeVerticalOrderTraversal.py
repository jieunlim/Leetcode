# T: O(n), S: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        sol = []
        dic = defaultdict(list)
        queue = deque()
        queue.append([root, 0])
        mincol = 0
        
        while queue:
            node, col = queue.popleft()
            dic[col].append(node.val)
        
            if node.left:
                queue.append([node.left, col-1])
                mincol = min(mincol, col-1)

            if node.right:
                queue.append([node.right, col+1])
                
        return [dic[key] for key in range(mincol, mincol + len(dic)]
                                          
#         for i in range(mincol, mincol + len(dic)):
#             sol.append(dic[i])
            
#         return sol
