# ======================================
# LeetCode Problem: range sum of bst
# Language: python3
# Link: https://leetcode.com/problems/range-sum-of-bst/
# Synced by: LinkCode
# Date: 03/07/2026, 23:59:32
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
            else:
                left = dfs(root.left)
                right = dfs(root.right)

            if low <= root.val <= high:
                return root.val + left + right
            else:
                return left + right
        
        return dfs(root)
