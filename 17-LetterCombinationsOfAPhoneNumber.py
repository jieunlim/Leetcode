# T: O(3^N*4^M)
# N is the number of digits in the input that maps to 3 letters(2, 3,4,5,6,8)
# M is the number of digits in the input that maps to 4 letters(7,9)
# space O(3^N*4^M)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        def dfs(index, path):
            
            if len(path) == len(digits):
                res.append(path)
                return
            for ch in dic[digits[index]]:
                dfs(index+1, path + ch)  
                
        if not digits:
            return []
        
        
        res = []
        dfs(0, "")
        return res
