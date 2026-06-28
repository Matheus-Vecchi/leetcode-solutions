# ======================================
# LeetCode Problem: count good nodes in binary tree
# Language: python3
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Synced by: LinkCode
# Date: 28/06/2026, 15:55:28
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_node = root.val
        def dfs(root, max_node):
            if not root:
                return 0
            
            if root.val >= max_node:
                acc = 1
                max_node = root.val
            else:
                acc = 0
            
            left = dfs(root.left, max_node)
            right = dfs(root.right, max_node)

            return acc + left + right
        
        return dfs(root, max_node)
