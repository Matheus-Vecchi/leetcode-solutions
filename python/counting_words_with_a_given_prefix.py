# ======================================
# LeetCode Problem: counting words with a given prefix
# Language: python3
# Link: https://leetcode.com/problems/counting-words-with-a-given-prefix/
# Synced by: LinkCode
# Date: 24/07/2026, 11:38:09
# ======================================


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        end = len(pref)
        count = 0

        for word in words:
            if word[:end] == pref:
                count += 1

        return count