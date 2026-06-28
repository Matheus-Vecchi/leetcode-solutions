# ======================================
# LeetCode Problem: find peak element
# Language: python3
# Link: https://leetcode.com/problems/find-peak-element/
# Synced by: LinkCode
# Date: 28/06/2026, 00:43:16
# ======================================


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                l = mid + 1
            if mid == len(nums) - 1:
                if nums[mid] > nums[mid-1]:
                    return mid
                r = mid - 1
                
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] > nums[mid-1]:
                l = mid + 1
            elif nums[mid] < nums[mid-1]:
                r = mid - 1
        
        return l