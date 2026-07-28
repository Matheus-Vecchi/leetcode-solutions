# ======================================
# LeetCode Problem: convert sorted array to binary search tree
# Language: python3
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Synced by: LinkCode
# Date: 28/07/2026, 12:48:54
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(root, lowest, highest):
            if lowest > highest:
                return None

            mid = (lowest + highest) // 2
            root = TreeNode(nums[mid])

            root.left = dfs(root.left, lowest, mid - 1)
            root.right = dfs(root.right, mid + 1, highest)

            return root
        
        return dfs(TreeNode(nums[(0 + len(nums) - 1) // 2]), 0, len(nums) - 1)