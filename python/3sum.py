# ======================================
# LeetCode Problem: 3sum
# Language: python3
# Link: https://leetcode.com/problems/3sum/
# Synced by: LinkCode
# Date: 28/05/2026, 09:51:52
# ======================================


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i = 0
        l = 1
        r = len(nums) - 1

        while i < len(nums) - 2:
            if nums[i] > 0:
                return ans
            
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
            l = i+1
            r = len(nums) - 1

        return ans
