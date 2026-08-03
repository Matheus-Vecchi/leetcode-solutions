# ======================================
# LeetCode Problem: add two numbers ii
# Language: python3
# Link: https://leetcode.com/problems/add-two-numbers-ii/
# Synced by: LinkCode
# Date: 02/08/2026, 22:25:04
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        prev1 = None
        curr2 = l2
        prev2 = None

        while curr1:
            aux = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = aux
        l1 = prev1
        
        while curr2:
            aux = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = aux
        l2 = prev2

        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry == 1:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0

            result = v1 + v2 + carry

            if result > 9:
                result -= 10
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(result)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        curr.next = l1 or l2
    
        

        curr = dummy.next
        prev = None
        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux

        return prev