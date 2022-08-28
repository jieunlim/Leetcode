# O(nlogn)
# O(n)

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue=deque([(root, 0)])
        dic = defaultdict(list)
        mincol = 0
        
        while queue:
            level = []
            for node, col in queue:
                dic[col].append(node.val)
                
                if node.left:
                    level.append((node.left, col-1))
                    mincol = min(mincol, col-1)
                if node.right:
                    level.append((node.right, col+1))
            level.sort(key = lambda x: x[0].val)
            queue = level
            
        for i in range(len(dic)):
            res.append(dic[mincol + i])
        return res
        
        

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [(root, 0)]
        mincol = 0
        dic = defaultdict(list)
        sol = []
        
        while queue:
            lqueue = []
            ldic = defaultdict(list)
            
            for node, col in queue:
                ldic[col].append(node.val)
                if node.left: 
                    lqueue.append((node.left, col-1))
                    mincol = min(mincol, col-1)
                if node.right: lqueue.append((node.right, col+1))
                    
            for i in ldic:
                dic[i].extend(sorted(ldic[i]))
            queue = lqueue
        
        for i in range(len(dic)):
            sol.append(dic[mincol + i])
        
        return sol

from collections import deque
from collections import defaultdict

class Solution2:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [(root, 0)]
        dic = defaultdict(list)
        sol = []
        
        while queue:
            lqueue = []
            ldic = defaultdict(list)
            
            for node, col in queue:
                ldic[col].append(node.val)
                if node.left: lqueue.append((node.left, col-1))
                if node.right: lqueue.append((node.right, col+1))
                    
            for i in ldic:
                dic[i].extend(sorted(ldic[i]))
            queue = lqueue
        
        return [dic[x] for x in sorted(dic)]
                    
        
        
