# ======================================
# LeetCode Problem: merge two binary trees
# Language: python3
# Link: https://leetcode.com/problems/merge-two-binary-trees/
# Synced by: LinkCode
# Date: 03/07/2026, 17:45:04
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root3 = TreeNode(0)

        def dfs(root1, root2, root3):
            if not root1 and not root2:
                return None

            if root1 and root2:
                root3 = TreeNode(root1.val + root2.val)
                root3.left = dfs(root1.left, root2.left, root3.left)
                root3.right = dfs(root1.right, root2.right, root3.right)
            
            if not root1:
                root3 = TreeNode(root2.val)
                root3.left = dfs(None, root2.left, root3.left)
                root3.right = dfs(None, root2.right, root3.right)
            if not root2:
                root3 = TreeNode(root1.val)
                root3.left = dfs(root1.left, None, root3.left)
                root3.right = dfs(root1.right, None, root3.right)              
            
            return root3
            
        return dfs(root1, root2, root3)
        
