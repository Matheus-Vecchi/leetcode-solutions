# ======================================
# LeetCode Problem: 3sum closest
# Language: python3
# Link: https://leetcode.com/problems/3sum-closest/
# Synced by: LinkCode
# Date: 05/07/2026, 23:09:20
# ======================================


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        i = 0
        l = i + 1
        r = len(nums) - 1

        closest_sum = [999999999999999, 999999999999999999]

        while i < len(nums) - 2:
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                diff = abs(current_sum - target)

                if diff < closest_sum[0]:
                    closest_sum = [diff, current_sum]
                
                if current_sum > target:
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    return target
            
            i += 1
            l = i + 1
            r = len(nums) - 1

        return closest_sum[1]