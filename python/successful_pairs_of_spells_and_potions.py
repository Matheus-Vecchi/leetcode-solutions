# ======================================
# LeetCode Problem: successful pairs of spells and potions
# Language: python3
# Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Synced by: LinkCode
# Date: 12/07/2026, 03:00:12
# ======================================


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        ans = []

        for spell in spells:
            ans.append(self.aux(spell, potions, success))
        
        return ans
            

    def aux(self, spell, potions, success):
        l = 0
        r = len(potions) - 1

        last_mid = len(potions)

        while l <= r:
            mid = (l+r) // 2

            if potions[mid] * spell >= success:
                last_mid = mid
                r = mid - 1
            else:
                l = mid + 1
        
        if last_mid != len(potions):
            return len(potions) - 1 - last_mid + 1
        else:
            return 0

        
