# ======================================
# LeetCode Problem: online stock span
# Language: python3
# Link: https://leetcode.com/problems/online-stock-span/
# Synced by: LinkCode
# Date: 28/06/2026, 01:07:44
# ======================================


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])

        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)