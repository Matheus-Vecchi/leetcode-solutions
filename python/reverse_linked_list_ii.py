# ======================================
# LeetCode Problem: reverse linked list ii
# Language: python3
# Link: https://leetcode.com/problems/reverse-linked-list-ii/
# Synced by: LinkCode
# Date: 24/05/2026, 18:49:16
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        l_prev = dummy
        for i in range(left-1):
            l_prev = l_prev.next
        

        r_next = dummy
        for i in range(right):
            r_next = r_next.next
        r_next = r_next.next


        curr = l_prev.next
        prev = None
        while curr != r_next:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        

        l_prev.next.next = curr
        l_prev.next = prev
        
        return dummy.next
