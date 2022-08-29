# 515
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#BFS, Level order - T:O(n), S: O(D) d: tree diameter to keep queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([(root, 1)])
        res = []
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
            res.append(node.val)
        return res
    
    
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([(root, 1)])
        res = []
        while queue:
            cur = []
            for _ in range(len(queue)):
                node, level = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
            res.append(cur[-1])
        return res

#DFS T: O(n), S: O(h), recursive stack
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        res = []
        def dfs(node, level):
            if not node: return
            if len(res) == level: res.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        dfs(root, 0)
        return res
    
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        def helper(node, level):
            if level == len(res): res.append(node.val)
            for child in (node.right, node.left):
                if child:
                    helper(child, level + 1)
        helper(root, 0)
        return res    
    
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
        if not root: return []
        sol = [root.val]
        queue = deque([(root, 0)])
        while queue:
            curlevel = []
            for node, level in queue:
                if node.left:
                    curlevel.append((node.left, level+1))
                if node.right:
                    curlevel.append((node.right, level+1))
            if curlevel: sol.append(curlevel[-1][0].val)
            queue = curlevel

        return sol
    
class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        def helper(node, level):
            if len(ans)==level:
                ans.append(node.val)
            if node.right:
                helper(node.right, level +1)
            if node.left:
                helper(node.left, level+1)
            
        helper(root, 0)
        return ans
