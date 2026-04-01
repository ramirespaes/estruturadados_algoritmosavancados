class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Avança o fast n+1 passos
        for _ in range(n + 1):
            fast = fast.next

        # Move os dois ponteiros
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove o nó
        slow.next = slow.next.next

        return dummy.next
