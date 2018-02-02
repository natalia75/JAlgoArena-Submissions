class Solution:
    def deleteTailNode(self, head):
        if not head:
            return head
        if not head.next:
            return head

        pre_tail = head

        while pre_tail.next.next:
          pre_tail = pre_tail.next

        pre_tail.next = None
        return head
