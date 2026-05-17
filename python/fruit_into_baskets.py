# ======================================
# LeetCode Problem: fruit into baskets
# Language: python3
# Link: https://leetcode.com/problems/fruit-into-baskets/
# Synced by: LinkCode
# Date: 17/05/2026, 17:08:51
# ======================================


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        seq = {}
        ans = 1

        for r in range(len(fruits)):
            if fruits[r] in seq:
                seq[fruits[r]] += 1
            else:
                seq[fruits[r]] = 1

            while len(seq) > 2:
                if seq[fruits[l]] == 1:
                    seq.pop(fruits[l])
                else:
                    seq[fruits[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans


