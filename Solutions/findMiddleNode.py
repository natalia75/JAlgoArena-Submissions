class Solution:
    def findMiddleNode(self, head):
        if not head:
            return head
        if not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
