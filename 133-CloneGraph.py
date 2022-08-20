class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node] = Node(node.val)
            
            for n in node.neighbors:
                new = dfs(n)
                visited[node].neighbors.append(new)
            return visited[node]
        
        return dfs(node)
