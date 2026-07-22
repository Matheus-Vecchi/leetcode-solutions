# ======================================
# LeetCode Problem: path sum iii
# Language: python3
# Link: https://leetcode.com/problems/path-sum-iii/
# Synced by: LinkCode
# Date: 22/07/2026, 18:08:12
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(root, acc, prefix):
            if not root:
                return 0
            
            count = 0
            
            acc += root.val

            if acc - targetSum in prefix:
                count = prefix[acc - targetSum]

            if acc not in prefix:
                prefix[acc] = 1
            else:
                prefix[acc] += 1

            left = dfs(root.left, acc, prefix)
            right = dfs(root.right, acc, prefix)

            prefix[acc] -= 1

            return left + right + count

        return dfs(root, 0, prefix)
