# ======================================
# LeetCode Problem: sum root to leaf numbers
# Language: python3
# Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Synced by: LinkCode
# Date: 03/07/2026, 23:06:52
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        acc = 0
        def dfs(root, number):
            nonlocal acc
            if not root:
                return

            number = number + str(root.val)

            if not root.left and not root.right:
                acc += int(number)
            
            dfs(root.left, str(number))
            dfs(root.right, str(number))
        
        dfs(root, "")
        return acc
