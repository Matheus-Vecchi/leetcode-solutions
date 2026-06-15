# ======================================
# LeetCode Problem: remove duplicates from sorted list
# Language: python3
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Synced by: LinkCode
# Date: 15/06/2026, 17:01:24
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr != None:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        
        return head
