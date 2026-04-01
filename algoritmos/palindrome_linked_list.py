class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    left = head
    right = prev

    while right:
        if left.val != right.val:
            print(f"❌ Não é palíndromo! Divergência: {left.val} != {right.val}")
            return False
        left = left.next
        right = right.next

    print(f"✅ É um palíndromo!")
    return True


# Teste 1 — palíndromo par: 1 → 2 → 2 → 1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
print("Teste 1:", isPalindrome(node1))


# Teste 2 — não é palíndromo: 1 → 2 → 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
print("Teste 2:", isPalindrome(node1))


# Teste 3 — único nó: 7
node1 = ListNode(7)
print("Teste 3:", isPalindrome(node1))
