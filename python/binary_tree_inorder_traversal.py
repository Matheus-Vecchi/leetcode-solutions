# ======================================
# LeetCode Problem: binary tree inorder traversal
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Synced by: LinkCode
# Date: 21/07/2026, 16:04:19
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return []
            
            left = dfs(root.left)
            right = dfs(root.right)

            return left + [root.val] + right
        
        return dfs(root)