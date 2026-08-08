# ======================================
# LeetCode Problem: reorder list
# Language: python3
# Link: https://leetcode.com/problems/reorder-list/
# Synced by: LinkCode
# Date: 07/08/2026, 21:24:06
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
    

        curr = mid
        prev = None
        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        l2 = prev

        dummy = head
        l1 = head
        while l1 and l2:
            aux1 = l1.next
            aux2 = l2.next

            l1.next = l2
            l2.next = aux1
            
            l1 = aux1
            l2 = aux2
        
        return dummy





        