#dic 사용, 0이 아닌수만 곱해주자.

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        #res = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        res = [[0]*len(mat2[0]) for _ in range(len(mat1))]  # len(mat1) * len(mat2[0])
        print(len(res), len(res[0]))
        print(res)
        dic1 = {}
        dic2 = {}
        
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if mat1[i][j] != 0:
                    dic1[(i, j)]= mat1[i][j]
        
        for i in range(len(mat2)):
            for j in range(len(mat2[0])):
                if mat2[i][j] != 0:
                    dic2[(i, j)] = mat2[i][j]
        
        
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                     
                    a = mat1[i][k] if (i, k) in dic1 else 0
                    b = mat2[k][j] if (k, j) in dic2 else 0
                    res[i][j] += a * b
                
                
        return res
        
