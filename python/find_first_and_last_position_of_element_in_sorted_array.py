# ======================================
# LeetCode Problem: find first and last position of element in sorted array
# Language: python3
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Synced by: LinkCode
# Date: 26/05/2026, 16:05:30
# ======================================


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        ans = [-1, -1]

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    ans[0] = mid
                    break
                else:
                    r = mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    ans[1] = mid
                    break
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans