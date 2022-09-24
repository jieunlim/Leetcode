#T: O(n), S: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = float('-inf')
        
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > minprice:
                max_profit = max(max_profit, prices[i]-minprice)
            minprice = min(minprice, prices[i])
        return max_profit
