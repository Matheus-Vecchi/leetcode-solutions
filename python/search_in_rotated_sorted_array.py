# ======================================
# LeetCode Problem: search in rotated sorted array
# Language: python3
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Synced by: LinkCode
# Date: 05/06/2026, 17:54:30
# ======================================


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
