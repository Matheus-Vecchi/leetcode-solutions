# ======================================
# LeetCode Problem: validate binary search tree
# Language: python3
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Synced by: LinkCode
# Date: 30/07/2026, 21:41:50
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        
        def dfs(root):
            nonlocal arr

            if not root:
                return True
            
            left = dfs(root.left)
            if arr and root.val <= arr[-1]:
                return False
            arr.append(root.val)
            right = dfs(root.right)

            return left and right

        return dfs(root)
        