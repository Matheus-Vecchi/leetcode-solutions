# ======================================
# LeetCode Problem: invert binary tree
# Language: python3
# Link: https://leetcode.com/problems/invert-binary-tree/
# Synced by: LinkCode
# Date: 12/06/2026, 17:23:42
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
