# ======================================
# LeetCode Problem: path sum
# Language: python3
# Link: https://leetcode.com/problems/path-sum/
# Synced by: LinkCode
# Date: 14/08/2026, 23:16:30
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, acc):
            if not root:
                return False
            
            acc += root.val
            if not root.left and not root.right and acc == targetSum:
                return True
            
            left = dfs(root.left, acc)
            right = dfs(root.right, acc)

            return left or right
        
        return dfs(root, 0)
