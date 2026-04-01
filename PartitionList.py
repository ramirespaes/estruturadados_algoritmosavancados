# Definição para um nó da lista encadeada (padrão LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Criamos dois "Dummy Nodes" (nós fictícios) para iniciar as duas listas
        # after_head guardará nós >= x, before_head guardará nós < x
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Ponteiros para percorrer e montar as novas listas
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                # Adiciona à lista de menores
                before.next = curr
                before = before.next
            else:
                # Adiciona à lista de maiores ou iguais
                after.next = curr
                after = after.next
            
            # Move para o próximo nó da lista original
            curr = curr.next
            
        # Importante: O último nó da lista 'after' deve apontar para None
        # Caso contrário, pode criar um ciclo infinito na lista final
        after.next = None
        
        # Conecta o fim da lista 'before' com o início da lista 'after'
        # Pulamos o nó fictício (after_head.next)
        before.next = after_head.next
        
        # Retornamos a lista começando pelo primeiro elemento real de 'before'
        return before_head.next