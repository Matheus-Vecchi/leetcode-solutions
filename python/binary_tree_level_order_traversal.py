# ======================================
# LeetCode Problem: binary tree level order traversal
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Synced by: LinkCode
# Date: 05/07/2026, 15:11:08
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []

        if root:
            queue.append(root)
        
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(level)

        return ans
                
