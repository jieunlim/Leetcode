# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#O(n), O(n)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def build(node, p = None):
            if not node: return
            parent[node] = p
            build(node.left, node)
            build(node.right, node)
        
        build(root)
        
        queue = deque([(target, k)])
        seen = set()
        res = []
        
        while queue:
            node, k = queue.popleft()
            if node:
                if k == 0: res.append(node.val)
                seen.add(node)
                for n in (node.left, node.right, parent[node]):
                    if n not in seen:
                        queue.append((n, k-1))
        return res

    
    
class Solution2:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj = defaultdict(list) # node: neighbors
        def buildgraph(node):
            if not node: return
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                buildgraph(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                buildgraph(node.right)
                
                
        buildgraph(root)
        
        sol = []
        visited = set()
        visited.add(target)
        
        def dfs(node, d):
            if d == 0:
                sol.append(node.val)
                return
            visited.add(node)
            for n in adj[node]:
                if n not in visited:
                    dfs(n, d-1)
        dfs(target, k)
        
        return sol
