# ======================================
# LeetCode Problem: count good nodes in binary tree
# Language: python3
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Synced by: LinkCode
# Date: 29/06/2026, 23:10:40
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
        ans = 0

        def dfs(root, max_seen):
            nonlocal ans

            if not root:
                return 0
            
            if root.val >= max_seen:
                ans += 1
                max_seen = root.val
            
            dfs(root.left, max_seen)
            dfs(root.right, max_seen)
        
        dfs(root, max_seen)
        return ans