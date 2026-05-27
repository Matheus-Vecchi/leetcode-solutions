# ======================================
# LeetCode Problem: count the number of special characters ii
# Language: python3
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-ii/
# Synced by: LinkCode
# Date: 27/05/2026, 17:28:09
# ======================================


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        uppercases = {}
        ans = set()

        for c in range(len(word)):
            if word[c].isupper():
                if word[c] not in uppercases:
                    uppercases[word[c]] = c
        
        for c in range(len(word)):
            if word[c].islower():
                if word[c].upper() in uppercases:
                    ans.add(word[c].upper())
                    if c > uppercases[word[c].upper()]:
                        ans.remove(word[c].upper())
                
                    
        return len(ans)
