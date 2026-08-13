# ======================================
# LeetCode Problem: smallest subtree with all the deepest nodes
# Language: python3
# Link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Synced by: LinkCode
# Date: 13/08/2026, 20:37:49
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root, depth):
            if not root:
                return (0, None)
            
            if not root.left and not root.right:
                return (depth, root)
            
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

            if left[0] == right[0]:
                return (left[0], root)
            elif left[0] > right[0]:
                return (left[0], left[1])
            else:
                return (right[0], right[1])
        
        return dfs(root, 0)[1]

