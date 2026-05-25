# ======================================
# LeetCode Problem: koko eating bananas
# Language: python3
# Link: https://leetcode.com/problems/koko-eating-bananas/
# Synced by: LinkCode
# Date: 24/05/2026, 22:07:06
# ======================================


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low < high:
            mid = (low+high) // 2
            if self.validAmount(mid, piles, h):
                ans = mid
                high = mid
            else:
                low = mid + 1
        
        return ans


    def validAmount(self, mid, piles, h):
        wasted_hours = 0

        for b in piles:
            hours = (b + mid - 1) // mid
            wasted_hours += hours
        
        if wasted_hours <= h:
            return True
        else:
            return False
