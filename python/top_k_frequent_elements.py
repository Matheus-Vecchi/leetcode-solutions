# ======================================
# LeetCode Problem: top k frequent elements
# Language: python3
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Synced by: LinkCode
# Date: 07/08/2026, 22:58:37
# ======================================


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key, value in hashmap.items():
            bucket[value].append(key)
        
        count = 0
        ans = []

        for freq in range(len(bucket)-1, -1, -1):
            for num in bucket[freq]:
                count += 1
                ans.append(num)
                if count == k:
                    return ans
