# ======================================
# LeetCode Problem: median of two sorted arrays
# Language: python3
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Synced by: LinkCode
# Date: 12/06/2026, 11:14:52
# ======================================


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []

        n1 = 0
        n2 = 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] <= nums2[n2]:
                nums.append(nums1[n1])
                n1 += 1
            else:
                nums.append(nums2[n2])
                n2 += 1
        
        if n1 < len(nums1):
            aux = nums1[n1:]

        else:
            aux = nums2[n2:]
        
        nums.extend(aux)

        middle = len(nums) // 2

        if len(nums) % 2 == 0:
            middle2 = middle - 1
            median = (nums[middle2] + nums[middle]) / 2
            return median
        else:
            median = nums[middle]
            return median

            

        

