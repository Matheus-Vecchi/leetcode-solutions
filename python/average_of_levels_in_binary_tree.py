# ======================================
# LeetCode Problem: average of levels in binary tree
# Language: python3
# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Synced by: LinkCode
# Date: 18/07/2026, 17:21:35
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        ans = []

        def dfs(root, level):
            if not root:
                return
            
            if level == len(levels):
                levels.append([])
            
            levels[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        
        for level in range(len(levels)):
            acc = 0
            for num in levels[level]:
                acc += num
            ans.append(acc / len(levels[level]))
        
        return ans