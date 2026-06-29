# ======================================
# LeetCode Problem: maximum depth of binary tree
# Language: python3
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Synced by: LinkCode
# Date: 29/06/2026, 12:01:26
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
