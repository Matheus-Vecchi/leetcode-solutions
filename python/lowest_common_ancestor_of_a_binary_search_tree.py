# ======================================
# LeetCode Problem: lowest common ancestor of a binary search tree
# Language: python3
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Synced by: LinkCode
# Date: 23/07/2026, 12:56:21
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if curr == p or curr == q:
                return curr
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
