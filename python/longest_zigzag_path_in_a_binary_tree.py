# ======================================
# LeetCode Problem: longest zigzag path in a binary tree
# Language: python3
# Link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Synced by: LinkCode
# Date: 22/07/2026, 17:13:10
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, direction, length):
            nonlocal ans
            if not root:
                return 0
            
            ans = max(ans, length)
            
            if direction == 0:
                dfs(root.left, 0, 1)
                dfs(root.right, 1, length+1)
            elif direction == 1:
                dfs(root.left, 0, length+1)
                dfs(root.right, 1, 1)
            else:
                dfs(root.left, 0, length+1)
                dfs(root.right, 1, length+1)     
        
        dfs(root, -1, 0)
        return ans
