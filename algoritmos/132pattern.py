class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        # Se a lista tiver menos de 3 elementos, o padrão é impossível
        if len(nums) < 3:
            return False
        
        # O padrão 132 consiste em: nums[i] < nums[k] < nums[j] com i < j < k
        # Vamos chamar nums[k] de 'segundo_maior' (o valor "2" do padrão 132)
        stack = []
        segundo_maior = float('-inf')
        
        # Percorremos o array de trás para frente para encontrar o padrão
        for i in range(len(nums) - 1, -1, -1):
            # Se encontrarmos um número menor que o nosso 'segundo_maior',
            # encontramos o nums[i] (o "1" do padrão). Retornamos True.
            if nums[i] < segundo_maior:
                return True
            
            # Se o número atual for maior que o topo da pilha,
            # ele é um candidato a ser o nums[j] (o "3" do padrão).
            # Atualizamos o 'segundo_maior' com os valores da pilha que são menores que ele.
            while stack and nums[i] > stack[-1]:
                segundo_maior = stack.pop()
            
            # Adicionamos o número atual na pilha como um potencial nums[k]
            stack.append(nums[i])
            
        return False