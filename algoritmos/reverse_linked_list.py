class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseBetween(head, left, right):
    if not head:
        return None

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    current = prev.next

    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next

def lista_para_array(head):
    resultado = []
    while head:
        resultado.append(head.value)
        head = head.next
    return resultado

def array_para_lista(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


head = array_para_lista([1, 2, 3, 4, 5])
resultado = lista_para_array(reverseBetween(head, 2, 4))
assert resultado == [1, 4, 3, 2, 5], f"Erro: {resultado}"
print("Teste 1 passou:", resultado)


head = array_para_lista([5])
resultado = lista_para_array(reverseBetween(head, 1, 1))
assert resultado == [5], f"Erro: {resultado}"
print("Teste 2 passou:", resultado)


head = array_para_lista([1, 2, 3, 4, 5])
resultado = lista_para_array(reverseBetween(head, 1, 5))
assert resultado == [5, 4, 3, 2, 1], f"Erro: {resultado}"
print("Teste 3 passou:", resultado)

print("\nTodos os testes passaram!")