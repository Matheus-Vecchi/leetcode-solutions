# ======================================
# LeetCode Problem: lowest common ancestor of a binary tree
# Language: python3
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Synced by: LinkCode
# Date: 29/06/2026, 17:32:46
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root.val == p.val:
            return root
        if root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left and not right:
            return left
        if not left and right:
            return right
            