# ======================================
# LeetCode Problem: lowest common ancestor of a binary search tree
# Language: python3
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Synced by: LinkCode
# Date: 23/07/2026, 12:10:37
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            if not root:
                return
            if root == p:
                return p
            if root == q:
                return q
            
            if root.val > p.val and root.val > q.val:
                left = dfs(root.left, p, q)
                right = None
            elif root.val < p.val and root.val < q.val:
                left = None
                right = dfs(root.right, p, q)
            else:
                left = dfs(root.left, p, q)
                right = dfs(root.right, p, q)
            
            if left and right:
                return root
            if not left:
                return right
            if not right:
                return left
        
        return dfs(root, p, q)