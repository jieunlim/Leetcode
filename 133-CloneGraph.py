class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
#dfs - recursion
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
    
    
#dfs - iterative  

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        stack = [node]
        m = {}
        visited = set()
        
        while stack:
            n = stack.pop()
            if n in visited: continue
            else: visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                stack.append(neigh)
                
        return m[node]
    
 #bfs
class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        
        visited = {node:Node(node.val)}
        queue = collections.deque([node])
        
        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)
                visited[cur].neighbors.append(visited[n])
                
                
        return visited[node]
