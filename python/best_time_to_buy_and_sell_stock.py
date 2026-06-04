# ======================================
# LeetCode Problem: best time to buy and sell stock
# Language: python3
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Synced by: LinkCode
# Date: 04/06/2026, 00:25:15
# ======================================


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            
            sell += 1
        
        return profit