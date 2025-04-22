# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head  

        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next

        k = k % len(values)
        if k == 0:
            return head  

        values = values[-k:] + values[:-k]

        new_head = ListNode(values[0])
        current = new_head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

        return new_head