# ======================================
# LeetCode Problem: longest common prefix
# Language: python3
# Link: https://leetcode.com/problems/longest-common-prefix/
# Synced by: LinkCode
# Date: 20/08/2026, 16:19:48
# ======================================


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = strs[0]
        
        for i in range(len(strs)):
            if len(strs[i]) < len(smallest):
                smallest = strs[i]
        
        i = 0
        j = 1

        while i < len(smallest): # i = 0
            while j < len(strs): # j = 1
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
                j += 1
            i += 1
            j = 1
        
        return smallest

        

