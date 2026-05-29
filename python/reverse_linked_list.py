# ======================================
# LeetCode Problem: reverse linked list
# Language: python3
# Link: https://leetcode.com/problems/reverse-linked-list/
# Synced by: LinkCode
# Date: 29/05/2026, 10:39:11
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev