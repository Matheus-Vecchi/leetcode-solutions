# ======================================
# LeetCode Problem: delete node in a bst
# Language: python3
# Link: https://leetcode.com/problems/delete-node-in-a-bst/
# Synced by: LinkCode
# Date: 29/06/2026, 18:32:59
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            elif not root.left and not root.right:
                return None
            else:
                new_node = self.findMinimun(root.right)
                root.right = self.deleteNode(root.right, new_node.val)
                root.val = new_node.val

        return root
    

    def findMinimun(self, root):
        while root.left:
            root = root.left
        return root
