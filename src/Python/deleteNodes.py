class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current = head

        while current:
            for _ in range(1, m):
                if current is None:
                    return head
                current = current.next

            if current is None or current.next is None:
                return head

            temp = current.next
            for _ in range(n):
                if temp is None:
                    break
                temp = temp.next

            current.next = temp
            current = temp

        return head
