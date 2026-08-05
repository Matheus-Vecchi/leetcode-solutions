# ======================================
# LeetCode Problem: minimum window substring
# Language: python3
# Link: https://leetcode.com/problems/minimum-window-substring/
# Synced by: LinkCode
# Date: 05/08/2026, 20:51:02
# ======================================


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window = {}
        hashmap_t = {}
        ans = s + "a"
        have = 0
        contains = True

        l = 0

        for i in t:
            if i not in hashmap_t:
                hashmap_t[i] = 1
            else:
                hashmap_t[i] += 1

        for r in range(len(s)):
            if not window and s[r] not in hashmap_t:
                l += 1
            
            if s[r] in hashmap_t:
                if s[r] not in window:
                    window[s[r]] = 1
                else:
                    window[s[r]] += 1
                have += 1

                while have >= len(t) and len(window) == len(hashmap_t):
                    contains = True
                    for k, v in window.items():
                        if window[k] < hashmap_t[k]:
                            contains = False
                            break

                    if contains:
                        if len(s[l:r]) < len(ans):
                            ans = s[l:r+1]
                        if window[s[l]] == 1:
                            del window[s[l]]
                        else:
                            window[s[l]] -= 1
                        have -= 1
                        l += 1
                        while l < len(s) and s[l] not in hashmap_t:
                            l += 1
                    else:
                        break
        
        if ans == s + "a":
            return ""
        else:
            return ans