class Solution(object):
    def flatten(self, head):
        curr = head

        def flat(node):
            curr = node
            tail = node

            while curr:
                nxt = curr.next
                if curr.child:
                    child_head = curr.child
                    curr.child = None
                    child_tail = flat(child_head)

                    curr.next = child_head
                    child_head.prev = curr

                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    tail = child_tail
                    curr = nxt
                else:
                    tail = curr
                    curr = nxt

            return tail

        flat(head)
        return head
