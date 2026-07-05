# ======================================
# LeetCode Problem: maximum width of binary tree
# Language: python3
# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
# Synced by: LinkCode
# Date: 05/07/2026, 16:30:31
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        max_width = 1

        if root:
            queue.append((root, 0))
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr[0].left:
                    queue.append((curr[0].left, curr[1] * 2))
                if curr[0].right:
                    queue.append((curr[0].right, curr[1] * 2 + 1))
            
            if queue:
                width = queue[-1][1] - queue[0][1] + 1
                max_width = max(max_width, width)

        return max_width
