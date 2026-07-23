# ======================================
# LeetCode Problem: lowest common ancestor of a binary search tree
# Language: python3
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Synced by: LinkCode
# Date: 23/07/2026, 12:38:16
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
            
            left = None
            right = None

            if not p:
                if root.val > q.val:
                    left = dfs(root.left, None, q)
                else:
                    right = dfs(root.right, None, q)
            elif not q:
                if root.val > p.val:
                    left = dfs(root.left, p, None)
                else:
                    right = dfs(root.right, p, None)
            else:
                if root.val > p.val and root.val > q.val:
                    left = dfs(root.left, p, q)
                elif root.val < p.val and root.val < q.val:
                    right = dfs(root.right, p, q)
                elif root.val > p.val:
                    left = dfs(root.left, p, None)
                    right = dfs(root.right, None, q)
                else:
                    left = dfs(root.left, None, q)
                    right = dfs(root.right, p, None)
            
            if left and right:
                return root
            if not left:
                return right
            if not right:
                return left
        
        return dfs(root, p, q)
