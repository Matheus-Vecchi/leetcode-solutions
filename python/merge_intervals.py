# ======================================
# LeetCode Problem: merge intervals
# Language: python3
# Link: https://leetcode.com/problems/merge-intervals/
# Synced by: LinkCode
# Date: 27/08/2026, 21:08:57
# ======================================


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        print(self.overlap([1, 10], [2,6]))
        ans = []
        intervals = sorted(intervals)
        print(intervals)
        current_interval = intervals[0]

        for i in range(len(intervals)):
            if i < len(intervals) - 1:
                if self.overlap(current_interval, intervals[i+1]):
                    current_interval = self.mergeSegments(current_interval, intervals[i+1])
                    print("aa", current_interval)
                else:
                    ans.append(current_interval)
                    current_interval = intervals[i+1]
                    
        
        if not ans:
            ans.append(current_interval)

        if not self.overlap(current_interval, ans[-1]):
            ans.append(current_interval)

        return ans

    def overlap(self, arr_i, arr_j):
        if (arr_i[1] >= arr_j[0] and arr_i[1] <= arr_j[1]):
            return True
        if (arr_i[0] >= arr_j[0] and arr_i[0] <= arr_j[1]):
            return True
        if (arr_i[1] >= arr_j[1] and arr_i[0] <= arr_j[0]):
            return True
        return False
    
    def mergeSegments(self, arr_i, arr_j):
        start = min(arr_i[0], arr_j[0])
        end = max(arr_i[1], arr_j[1])
        
        merged_interval = [start, end]
        print(arr_i, arr_j)
        print(merged_interval)
        return merged_interval

