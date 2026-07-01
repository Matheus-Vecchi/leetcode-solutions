# ======================================
# LeetCode Problem: maximum depth of binary tree
# Language: python3
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Synced by: LinkCode
# Date: 01/07/2026, 15:53:21
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            return 1 + max(right, left)
        
        return dfs(root)
        
        