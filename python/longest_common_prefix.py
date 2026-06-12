# ======================================
# LeetCode Problem: longest common prefix
# Language: python3
# Link: https://leetcode.com/problems/longest-common-prefix/
# Synced by: LinkCode
# Date: 12/06/2026, 12:55:27
# ======================================


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = 1
        char = 0

        smaller_string = strs[0]
        smallest_string = len(strs[0])
        for i in strs:
            if len(i) < smallest_string:
                smallest_string = len(i)
                smaller_string = i



        while char < smallest_string:
            while string < len(strs):
                if strs[0][char] == strs[string][char]:
                    string += 1
                else:
                    return strs[0][:char]
            string = 1
            char += 1
        
        return smaller_string
        


