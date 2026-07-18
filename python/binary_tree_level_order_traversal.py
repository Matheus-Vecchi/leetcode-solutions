# ======================================
# LeetCode Problem: binary tree level order traversal
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Synced by: LinkCode
# Date: 18/07/2026, 16:28:48
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}

        def dfs(root, level):
            if not root:
                return
            
            if level not in levels:
                levels[level] = [root.val]
            else:
                levels[level].append(root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        ans = [0] * len(levels)

        for key, value in levels.items():
            ans[key] = value
        
        return ans