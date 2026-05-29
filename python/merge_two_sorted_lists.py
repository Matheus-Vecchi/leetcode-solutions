# ======================================
# LeetCode Problem: merge two sorted lists
# Language: python3
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Synced by: LinkCode
# Date: 29/05/2026, 11:00:17
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                curr.next = pointer1

                pointer1 = pointer1.next
            else:
                curr.next = pointer2

                pointer2 = pointer2.next
            
            curr = curr.next
        
        curr.next = pointer1 or pointer2

        return dummy.next