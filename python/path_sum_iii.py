# ======================================
# LeetCode Problem: path sum iii
# Language: python3
# Link: https://leetcode.com/problems/path-sum-iii/
# Synced by: LinkCode
# Date: 13/07/2026, 19:00:02
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        valid_paths = self.dfs(root, 0, targetSum)

        left = self.pathSum(root.left, targetSum)
        right = self.pathSum(root.right, targetSum)

        return valid_paths + right + left


    def dfs(self, root, current_sum, targetSum):
        if not root:
            return 0
        
        current_sum += root.val
        if current_sum == targetSum:
            count = 1
        else:
            count = 0
        
        left = self.dfs(root.left, current_sum, targetSum)
        right = self.dfs(root.right, current_sum, targetSum)

        if count != 0:
            return 1 + left + right
        else:
            return left + right
