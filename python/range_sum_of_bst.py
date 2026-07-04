# ======================================
# LeetCode Problem: range sum of bst
# Language: python3
# Link: https://leetcode.com/problems/range-sum-of-bst/
# Synced by: LinkCode
# Date: 04/07/2026, 00:01:14
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
            
            if root.val > high:
                return dfs(root.left)
            elif root.val < low:
                return dfs(root.right)
            return root.val + dfs(root.left) + dfs(root.right)

        
        return dfs(root)
