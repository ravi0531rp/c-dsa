"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 
"""
from typing import List, Optional
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        heap = []
        for idx in range(len(lists)):
            head = lists[idx]
            if head:
                heappush(heap, (head.val, idx, head))
        
        while heap:
            value , idx, node = heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(heap, (node.next.val, idx, node.next))
        return dummy.next
