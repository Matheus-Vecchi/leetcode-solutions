# ======================================
# LeetCode Problem: construct binary tree from preorder and inorder traversal
# Language: python3
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Synced by: LinkCode
# Date: 15/07/2026, 22:12:09
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        divisory = inorder.index(root.val)
        root.left = self.buildTree(preorder[preorder.index(root.val)+1:], inorder[:divisory])
        root.right = self.buildTree(preorder[divisory+1:], inorder[divisory+1:])

        return root
