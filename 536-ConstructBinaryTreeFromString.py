class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def helper(i):
            start = i
            if s[i] =='-': i += 1
            while i < len(s) and s[i].isdigit(): i += 1
            num = int(s[start:i])
            
            #left
            if i < len(s) and s[i] == '(':
                left, i = helper(i + 1)
                i += 1
            else: 
                left = None
            
            #right
            if i< len(s) and s[i] == '(':
                right, i = helper(i + 1)
                i += 1
            else:
                right = None
                
            return TreeNode(num, left, right), i
        
        if len(s)==0: return None  
        answer, _ = helper(0)
        return None if len(s)==0 else answer
