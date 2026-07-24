# ======================================
# LeetCode Problem: minimum depth of binary tree
# Language: python3
# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Synced by: LinkCode
# Date: 23/07/2026, 22:51:14
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level = 0

        if root:
            queue.append(root)
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                curr = queue.popleft()

                if not curr.left and not curr.right:
                    return level
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return level