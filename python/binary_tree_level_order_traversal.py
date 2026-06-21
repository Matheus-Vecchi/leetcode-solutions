# ======================================
# LeetCode Problem: binary tree level order traversal
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Synced by: LinkCode
# Date: 21/06/2026, 18:49:43
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if root:
            queue.append(root)
        
        while queue:
            layer = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                layer.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(layer)
        
        return ans
