# ======================================
# LeetCode Problem: balanced binary tree
# Language: python3
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Synced by: LinkCode
# Date: 29/06/2026, 16:47:43
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]

            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]