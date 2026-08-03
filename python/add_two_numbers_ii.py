# ======================================
# LeetCode Problem: add two numbers ii
# Language: python3
# Link: https://leetcode.com/problems/add-two-numbers-ii/
# Synced by: LinkCode
# Date: 02/08/2026, 23:22:36
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        ans = []

        while l1 or l2:
            if l1 is not None:
                v1 = l1.val
            else:
                v1 = None
            if l2 is not None:
                v2 = l2.val
            else:
                v2 = None
            
            if v1 is not None:
                stack1.append(v1)
            if v2 is not None:
                stack2.append(v2)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        carry = 0
        while stack1 or stack2 or carry == 1:
            if stack1:
                s1 = stack1[-1]
            else:
                s1 = 0
            if stack2:
                s2 = stack2[-1]
            else:
                s2 = 0

            result = s1 + s2 + carry

            if stack1:
                stack1.pop()
            if stack2:
                stack2.pop()
            
            if result > 9:
                ans.append(result - 10)
                carry = 1                    
            else:
                ans.append(result)
                carry = 0
        
        dummy = ListNode(0)
        curr = dummy

        stop = len(ans) * (-1)

        for i in range(1, len(ans)+1):
            curr.next = ListNode(ans[-i])
            curr = curr.next

        return dummy.next
  