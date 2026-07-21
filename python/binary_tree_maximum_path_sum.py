# ======================================
# LeetCode Problem: binary tree maximum path sum
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Synced by: LinkCode
# Date: 21/07/2026, 17:16:24
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def dfs(root):
            nonlocal ans

            if not root:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            ans = max(ans, left+right+root.val)

            return max(root.val + left, root.val + right)
        
        dfs(root)
        return ans
