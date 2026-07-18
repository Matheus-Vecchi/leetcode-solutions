# ======================================
# LeetCode Problem: binary tree level order traversal
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Synced by: LinkCode
# Date: 18/07/2026, 16:20:59
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = {}

        def dfs(root, level):
            if not root:
                return
            
            if level not in dict:
                dict[level] = [root.val]
            else:
                dict[level].append(root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        ans = [0] * len(dict)

        for key, value in dict.items():
            ans[key] = value
        
        return ans