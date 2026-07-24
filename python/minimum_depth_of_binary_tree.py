# ======================================
# LeetCode Problem: minimum depth of binary tree
# Language: python3
# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Synced by: LinkCode
# Date: 23/07/2026, 22:23:00
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 and right == 0:
            return 1
        if left == 0:
            return 1 + right
        if right == 0:
            return 1 + left
        
        return 1 + min(left, right)
