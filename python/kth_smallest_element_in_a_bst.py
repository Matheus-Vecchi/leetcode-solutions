# ======================================
# LeetCode Problem: kth smallest element in a bst
# Language: python3
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Synced by: LinkCode
# Date: 15/07/2026, 20:39:12
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None

        def dfs(root):
            nonlocal count, ans

            if not root:
                return
            
            dfs(root.left)
            if ans:
                return
            count += 1
            if count == k:
                ans = root.val
            dfs(root.right)

        
        dfs(root)
        return ans
