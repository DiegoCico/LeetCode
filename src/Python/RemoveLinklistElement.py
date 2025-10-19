# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        behind, ahead = dummy, head
        while ahead is not None:
            if ahead.val == val:
                print("removing val")
                behind.next = ahead.next
                ahead = ahead.next
            else:
                behind = ahead
                ahead = ahead.next
        return dummy.next
