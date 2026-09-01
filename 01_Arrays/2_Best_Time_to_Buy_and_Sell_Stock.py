# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            # sell & buy
            if prices[buy] > prices[sell]:
                buy = sell

            else:
                # profit check
                current_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, current_profit)
            sell += 1
        return max_profit
