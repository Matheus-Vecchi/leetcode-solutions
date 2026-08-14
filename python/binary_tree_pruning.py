# ======================================
# LeetCode Problem: binary tree pruning
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-pruning/
# Synced by: LinkCode
# Date: 13/08/2026, 21:29:07
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if not root.left and not root.right and root.val == 0:
                return None
            
            return root
        
        return dfs(root)




        
