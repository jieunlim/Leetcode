

"""
DFS로 하기, (left, node, right)
1. head 없으면 넣어주기
2. prev있으면 prev.right = node
3. node.left = prev
4. prev = node

head - prev(마지막노드) 연결

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
#O(n)/O(n)
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        self.head, self.prev = None, None
        
        def dfs(node):
            if not node: return
            dfs(node.left)
            if not self.head: self.head = node
            if self.prev: self.prev.right = node
            node.left = self.prev
            self.prev = node
            dfs(node.right)
            
            
        dfs(root)
        self.head.left = self.prev
        self.prev.right = self.head
        
        return self.head
                
