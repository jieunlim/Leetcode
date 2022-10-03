#O(n^2) / O(n^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows: return
        sol = [[1] * (i+1) for i in range(numRows)]
        for i in range(numRows):
            print('i: ', i)
            for j in range(1, i):
                sol[i][j] = sol[i-1][j-1] + sol[i-1][j]
        return sol
                
                
