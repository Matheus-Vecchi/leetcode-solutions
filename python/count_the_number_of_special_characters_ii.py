# ======================================
# LeetCode Problem: count the number of special characters ii
# Language: python3
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-ii/
# Synced by: LinkCode
# Date: 27/05/2026, 17:04:48
# ======================================


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hashmap = {}
        ans = set()

        for c in range(len(word)):
            if word[c].islower():
                if word[c] not in hashmap:
                    hashmap[word[c]] = [c]
                else:
                    hashmap[word[c]].append(c)
        
        for c in range(len(word)):
            if word[c].isupper():
                if word[c].lower() in hashmap:
                    if c > hashmap[word[c].lower()][-1]:
                        ans.add(word[c])
                    else:
                        del hashmap[word[c].lower()]
        
        return len(ans)
                        