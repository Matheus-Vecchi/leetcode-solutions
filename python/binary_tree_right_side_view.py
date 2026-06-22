# ======================================
# LeetCode Problem: binary tree right side view
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Synced by: LinkCode
# Date: 21/06/2026, 22:39:35
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        queue = deque()

        if root:
            queue.append(root)
        
        while queue:
            ans.append(queue[-1].val)
            for i in range(1, len(queue)+1):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return list(ans)
