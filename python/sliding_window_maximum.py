# ======================================
# LeetCode Problem: sliding window maximum
# Language: python3
# Link: https://leetcode.com/problems/sliding-window-maximum/
# Synced by: LinkCode
# Date: 14/05/2026, 23:38:27
# ======================================


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        ans = []
        l = 0
        r = 0
        
        while r < len(nums):
            while dq and nums[r] > dq[-1]:
                dq.pop()
            dq.append(nums[r])

            if r - l + 1 == k:
                ans.append(dq[0])
                if nums[l] == dq[0]:
                    dq.popleft()
                l += 1
            
            r += 1
        
        return ans