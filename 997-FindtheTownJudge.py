# T: O(n)
# S: O(n)

class Solution:

    def findJudge(self, N, trust) :
        
        if len(trust) < N-1:
            return -1
        
        num_trust = [0] * (N+1)
            
        for a, b in trust:
            num_trust[a]-=1
            num_trust[b]+=1
            
        for i in range(1, N+1):
            if num_trust[i] == N-1:
                return i
            
        return -1

obj = Solution()
trust = [[1,3], [2,3]]
N = 3
print(obj.findJudge(N, trust))