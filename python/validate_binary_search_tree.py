# ======================================
# LeetCode Problem: validate binary search tree
# Language: python3
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Synced by: LinkCode
# Date: 30/07/2026, 21:44:24
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last_node = float('-inf')
        
        def dfs(root):
            nonlocal last_node

            if not root:
                return True
            
            left = dfs(root.left)
            if root.val <= last_node:
                return False
            last_node = root.val
            right = dfs(root.right)

            return left and right

        return dfs(root)
        