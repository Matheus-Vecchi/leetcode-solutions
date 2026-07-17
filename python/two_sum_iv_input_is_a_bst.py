# ======================================
# LeetCode Problem: two sum iv input is a bst
# Language: python3
# Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Synced by: LinkCode
# Date: 17/07/2026, 14:42:22
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()

        def dfs(root):
            if not root:
                return False
            
            diff = k - root.val
            if diff in hashset:
                return True
            hashset.add(root.val)
            
            left = dfs(root.left)
            right = dfs(root.right)

            return left or right
        
        return dfs(root)
