class Solution:
    def revevrseList(self, head):
        previos=None
        current=haed
        while(current is not None):
            next = current.next
            current.next=previos
            previos = current
            current = next
        head = previous
        return head
