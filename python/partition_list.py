# ======================================
# LeetCode Problem: partition list
# Language: python3
# Link: https://leetcode.com/problems/partition-list/
# Synced by: LinkCode
# Date: 15/06/2026, 22:12:42
# ======================================


class Solution:
    def partition(self, head, x):
        curr = head
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_ll = less_dummy
        greater_ll = greater_dummy 

        while curr:
            if curr.val < x:
                less_ll.next = curr
                less_ll = less_ll.next
            else:
                greater_ll.next = curr
                greater_ll = greater_ll.next
            curr = curr.next

        greater_ll.next = None 
        less_ll.next = greater_dummy.next
        return less_dummy.next