# ======================================
# LeetCode Problem: binary tree zigzag level order traversal
# Language: python3
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Synced by: LinkCode
# Date: 14/08/2026, 21:03:19
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []
        height = 0

        if root:
            queue.append(root)
        
        while queue:
            height += 1
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if height % 2 != 0:
                ans.append(level)
            else:
                l = 0
                r = len(level) - 1

                while l < r:
                    level[l], level[r] = level[r], level[l]
                    l += 1
                    r -= 1
                ans.append(level)

        return ans
        