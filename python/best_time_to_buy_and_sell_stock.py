# ======================================
# LeetCode Problem: best time to buy and sell stock
# Language: python3
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Synced by: LinkCode
# Date: 27/08/2026, 14:04:34
# ======================================


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1

        return max_profit
