# ======================================
# LeetCode Problem: binary tree inorder traversal
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Synced by: LinkCode
# Date: 21/07/2026, 16:48:16
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        
        return ans