# ======================================
# LeetCode Problem: plus one
# Language: python3
# Link: https://leetcode.com/problems/plus-one/
# Synced by: LinkCode
# Date: 11/06/2026, 18:34:55
# ======================================


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        
        while carry == 1:
            if digits[i] + carry == 10:
                if i == 0:
                    digits[i] = 1
                    digits.append(0)
                    carry = 0
                else:
                    carry = 1
                    digits[i] = 0
                    i -= 1
            else:
                carry = 0
                digits[i] += 1
        
        return digits
