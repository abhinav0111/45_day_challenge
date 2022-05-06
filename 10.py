class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = 100000000000
        profit = 0
        for i in range(len(prices)):
            if mi > prices[i]:
                mi = prices[i]
            elif(mi < prices[i]):
                profit = max(profit, prices[i]-mi)
        return profit
