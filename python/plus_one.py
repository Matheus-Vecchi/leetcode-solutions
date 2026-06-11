# ======================================
# LeetCode Problem: plus one
# Language: python3
# Link: https://leetcode.com/problems/plus-one/
# Synced by: LinkCode
# Date: 11/06/2026, 18:50:09
# ======================================


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        
        while i >= 0 and carry == 1:
            if digits[i] + carry == 10:
                carry = 1
                digits[i] = 0
                i -= 1
            else:
                carry = 0
                digits[i] += 1
        
        if carry == 1:
            digits[0] = 1
            digits.append(0)
        
        return digits