#543
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res = 0
        
        def helper(node):
            if not node: return 0
            nonlocal res
            first = second = 0
            
            
            for child in node.children:
                depth = helper(child)
                if depth > first:
                    first, second = depth, first
                elif depth > second:
                    second = depth
            res = max(res, first+ second)
            return first + 1
            
        helper(root)
        return res
        
