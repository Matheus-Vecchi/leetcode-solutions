# ======================================
# LeetCode Problem: lowest common ancestor of a binary tree
# Language: python3
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Synced by: LinkCode
# Date: 23/07/2026, 11:36:23
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
        if root == p:
            return p
        if root == q:
            return q
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not right:
            return left
        if not left:
            return right
