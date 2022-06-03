# T: O(n), S: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2])+ cost[i]
        return min(dp[-1], dp[-2])
      
#S: O(1), T: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cost[0]
        cur = cost[1]
        
        for i in range(2, len(cost)):
            temp = cur
            cur = min(prev, cur) + cost[i]
            prev = temp
        return min(cur, prev)
