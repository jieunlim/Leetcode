#T: O(n)
#S: O(1)

#Same[i+1] = diff[i]
#diff[i+1] = diff[i] * (k-1) + Same[i] * (k-1)
class Solution:
    def numWays(self, n, k):
        if n ==1:
            return k
        
        same = k 
        diff = k * (k-1)

        for i in range(2, n):
            tmp = same
            same = diff
            diff = diff * (k-1) + tmp * (k-1)
        return same + diff
obj = Solution()
n = 7
k = 2
print(obj.numWays(n, k))