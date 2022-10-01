#543
Time: O(N)
Space: O(N)
    
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
   
Time: O(N)
Space: O(N)
    
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        self.maxD = 0
        def dfs(node):
            if not node or not node.children: 
                return 0 if not node else 1
            heap = []
            for n in node.children:
                depth = dfs(n)
                heappush(heap, depth)
                if len(heap) > 2:
                    heappop(heap)
            self.maxD = max(self.maxD, sum(heap))
            return max(heap) + 1
        
        dfs(root)
        return self.maxD
