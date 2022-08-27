#O(n), O(n)


class Solution:
    def __init__(self):
        self.visited = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val)
        
        self.visited[head] = node
        node.next =self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
    
