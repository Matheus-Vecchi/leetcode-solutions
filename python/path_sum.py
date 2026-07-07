# ======================================
# LeetCode Problem: path sum
# Language: python3
# Link: https://leetcode.com/problems/path-sum/
# Synced by: LinkCode
# Date: 07/07/2026, 16:07:44
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, current_sum):
            if not root:
                return False
            
            current_sum += root.val

            left = dfs(root.left, current_sum)
            right = dfs(root.right, current_sum)

            if not root.left and not root.right:
                if current_sum == targetSum:
                    return True
                else:
                    return False

            return left or right
        
        return dfs(root, 0)