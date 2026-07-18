# ======================================
# LeetCode Problem: average of levels in binary tree
# Language: python3
# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Synced by: LinkCode
# Date: 18/07/2026, 16:58:32
# ======================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        ans = []
        acc = 0

        if root:
            queue.append(root)
        
        while queue:
            for i in range(1, len(queue) + 1):
                curr = queue.popleft()
                acc += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(acc / i)
            acc = 0

        return ans