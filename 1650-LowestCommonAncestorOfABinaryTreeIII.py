"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        dic = defaultdict(int)
        node = p
        dic[node] = 0
        while node.parent:
            dic[node.parent] = 0
            node = node.parent
        
        node2 = q
        
        while node2:
            if node2 in dic: return node2
            node2 = node2.parent
            
        
