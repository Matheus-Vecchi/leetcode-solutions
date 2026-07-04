# ======================================
# LeetCode Problem: range sum of bst
# Language: python3
# Link: https://leetcode.com/problems/range-sum-of-bst/
# Synced by: LinkCode
# Date: 03/07/2026, 23:41:20
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if low <= root.val <= high:
                return root.val + left + right
            else:
                return left + right
        
        return dfs(root)
