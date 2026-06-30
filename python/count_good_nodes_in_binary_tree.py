# ======================================
# LeetCode Problem: count good nodes in binary tree
# Language: python3
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Synced by: LinkCode
# Date: 29/06/2026, 23:12:04
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_seen = root.val

        def dfs(root, max_seen):
            if not root:
                return 0
            
            if root.val >= max_seen:
                ans = 1
                max_seen = root.val
            else:
                ans = 0
            
            left = dfs(root.left, max_seen)
            right = dfs(root.right, max_seen)
        
            return left + right + ans
        
        return dfs(root, max_seen)
            