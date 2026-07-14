# ======================================
# LeetCode Problem: path sum iii
# Language: python3
# Link: https://leetcode.com/problems/path-sum-iii/
# Synced by: LinkCode
# Date: 13/07/2026, 23:52:48
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, current_sum, hashmap):
            if not root:
                return 0
            
            current_sum += root.val
            if current_sum - targetSum in hashmap:
                count = hashmap[current_sum - targetSum]
            else:
                count = 0
            if current_sum in hashmap:
                hashmap[current_sum] += 1
            else:
                hashmap[current_sum] = 1
            
            left = dfs(root.left, current_sum, hashmap)
            right = dfs(root.right, current_sum, hashmap)

            hashmap[current_sum] -= 1

            return count + left + right
        
        return dfs(root, 0, {0: 1})
