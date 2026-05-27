# ======================================
# LeetCode Problem: reorder list
# Language: python3
# Link: https://leetcode.com/problems/reorder-list/
# Synced by: LinkCode
# Date: 26/05/2026, 21:22:04
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = slow

        while curr != None:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        
        curr1 = head
        curr2 = prev

        while curr2 != slow:
            aux1 = curr1.next
            aux2 = curr2.next
            
            curr1.next = curr2
            curr2.next = aux1

            curr1 = aux1
            curr2 = aux2
        