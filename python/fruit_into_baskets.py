# ======================================
# LeetCode Problem: fruit into baskets
# Language: python3
# Link: https://leetcode.com/problems/fruit-into-baskets/
# Synced by: LinkCode
# Date: 28/06/2026, 00:28:00
# ======================================


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        empty_baskets = 2
        basket = {}
        ans = 0

        for r in range(len(fruits)):
            if fruits[r] not in basket:
                basket[fruits[r]] = 1
                empty_baskets -= 1
            else:
                basket[fruits[r]] += 1
            
            while empty_baskets < 0:
                if basket[fruits[l]] == 1:
                    del basket[fruits[l]]
                    empty_baskets += 1
                else:
                    basket[fruits[l]] -= 1
                l += 1

            ans = max(ans, r - l  + 1)

        return ans
