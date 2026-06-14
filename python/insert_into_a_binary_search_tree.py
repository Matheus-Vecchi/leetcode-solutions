# ======================================
# LeetCode Problem: insert into a binary search tree
# Language: python3
# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Synced by: LinkCode
# Date: 14/06/2026, 17:06:06
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #BASE CASE
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root