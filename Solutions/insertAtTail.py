class Solution:
    def insertAtTail(self, head, data):
        if not head:
            head = data
            data.next = None
            return head
        current = head
        while(current.next):
            current=current.next
        current.next = data
        data.next = None
        return head
