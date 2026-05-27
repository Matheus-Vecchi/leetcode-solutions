# ======================================
# LeetCode Problem: minimum window substring
# Language: python3
# Link: https://leetcode.com/problems/minimum-window-substring/
# Synced by: LinkCode
# Date: 27/05/2026, 13:33:02
# ======================================


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        l = 0
        hashmap = {}
        ans = ""
        
        hashmap_t = {}

        for c in t:
            if c not in hashmap_t:
                hashmap_t[c] = 1
            else:
                hashmap_t[c] += 1
        
        for r in range(len(s)):
            if s[r] in hashmap_t:
                if s[r] in hashmap:
                    hashmap[s[r]] += 1
                else:
                    hashmap[s[r]] = 1
            else:
                while l <= r and s[l] not in hashmap:
                    l += 1
            
            while all(hashmap.get(k, 0) >= v for k, v in hashmap_t.items()):
                if len(s[l:r]) < len(ans) or ans == "":
                    ans = s[l:r+1]

                if s[l] in hashmap:
                    if hashmap[s[l]] == 1:
                        del hashmap[s[l]]
                    else:
                        hashmap[s[l]] -= 1
                l += 1                
                while l <= r and s[l] not in hashmap_t:
                    l += 1
        
        if ans == "":
            return ""
        else:
            return ans
        
        #{a:1, b:1, c:1}
        #{a:1, b:1, c:1}