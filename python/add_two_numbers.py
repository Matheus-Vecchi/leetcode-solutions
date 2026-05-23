# ======================================
# LeetCode Problem: add two numbers
# Language: python3
# Link: https://leetcode.com/problems/add-two-numbers/
# Synced by: LinkCode
# Date: 22/05/2026, 22:30:02
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        ans = curr

        num1 = l1
        num2 = l2

        while num1 or num2:
            soma = curr.val

            if num1:
                soma += num1.val
            if num2:
                soma += num2.val

            if soma > 9:
                curr.val = soma - 10
                curr.next = ListNode(1)
            else:
                curr.val = soma

                if num1 and num1.next:
                    curr.next = ListNode(0)
                elif num2 and num2.next:
                    curr.next = ListNode(0)

            curr = curr.next
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next

        return ans
