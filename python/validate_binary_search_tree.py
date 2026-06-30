# ======================================
# LeetCode Problem: validate binary search tree
# Language: python3
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Synced by: LinkCode
# Date: 29/06/2026, 23:17:54
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = -99999999999999999
        max_val = 99999999999999999

        def dfs(root, min_val, max_val):
            if not root:
                return True
            
            if root.val >= max_val:
                return False
            if root.val <= min_val:
                return False

            left = dfs(root.left, min_val, root.val)
            right = dfs(root.right, root.val, max_val)

            return left and right
        
        return dfs(root, min_val, max_val)
