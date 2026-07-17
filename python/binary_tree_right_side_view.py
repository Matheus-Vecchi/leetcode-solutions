# ======================================
# LeetCode Problem: binary tree right side view
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Synced by: LinkCode
# Date: 17/07/2026, 15:18:26
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        ans = []

        if root:
            queue.append(root)
        
        while queue:
            ans.append(queue[-1].val)
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return ans
