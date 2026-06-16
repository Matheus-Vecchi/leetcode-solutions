# ======================================
# LeetCode Problem: partition list
# Language: python3
# Link: https://leetcode.com/problems/partition-list/
# Synced by: LinkCode
# Date: 15/06/2026, 21:53:13
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr1 = dummy
        curr2 = head

        dq = deque([])

        while curr2:
            if curr2.val >= x:
                dq.append(curr2)
                curr2 = curr2.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
                dummy = dummy.next
        
        for i in dq:
            dummy.next = i
            dummy = dummy.next
        
        dummy.next = None
        
        return curr1.next
        