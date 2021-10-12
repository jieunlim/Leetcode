class Solution():
    def isToeplitzMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m-1):
            for j in range(1, n-1):
                if matrix[i][j]!= matrix[i-1][j-1]:
                    return False
        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
obj = Solution()
print(obj.isToeplitzMatrix(matrix))