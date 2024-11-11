class Pilha:
    def __init__(self):
        # Usamos uma lista para representar a pilha, onde o último elemento é o topo.
        self.itens = []

    def empilhar(self, item):
        # Adiciona um item ao topo da pilha
        self.itens.append(item)

    def desempilhar(self):
        # Remove e retorna o item do topo da pilha se não estiver vazia, senão retorna None
        return self.itens.pop() if not self.esta_vazia() else None

    def esta_vazia(self):
        # Verifica se a pilha está vazia
        return len(self.itens) == 0

    def topo(self):
        # Retorna o item do topo da pilha sem removê-lo, se não estiver vazia
        return self.itens[-1] if not self.esta_vazia() else None

    def tamanho(self):
        # Retorna o número total de itens na pilha
        return len(self.itens)

    def __str__(self):
        # Retorna a representação da pilha para facilitar a visualização
        return str(self.itens)

# Classe Pilha:
# A classe `Pilha` é uma estrutura de dados que segue o conceito LIFO (Last In, First Out), onde o último item inserido é o primeiro a ser removido.
# Para isso, a lista `itens` é usada para armazenar os elementos, facilitando as operações no topo da pilha.
# 
# Métodos:
# - `empilhar`: Adiciona um item ao topo da pilha.
# - `desempilhar`: Remove e retorna o item do topo, se a pilha não estiver vazia.
# - `esta_vazia`: Verifica se a pilha está vazia, retornando True ou False.
# - `topo`: Retorna o item do topo sem removê-lo, permitindo ver o próximo item sem alterar a pilha.
# - `tamanho`: Retorna o número de itens na pilha, útil para saber quantos elementos ela possui.
# 
# O uso de uma lista para implementar a pilha é eficiente e simples, pois as operações no final da lista são rápidas e cumprem bem o papel de uma estrutura LIFO.

def ordenar_pilha(pilha):
    """
    Ordena uma pilha em ordem crescente usando uma pilha auxiliar.
    
    Parâmetros:
    pilha (Pilha): A pilha de notas a ser ordenada.
    
    Retorna:
    Pilha: A pilha ordenada em ordem crescente.
    """
    pilha_auxiliar = Pilha()

    # Processa todos os elementos da pilha original
    while not pilha.esta_vazia():
        # Remove o elemento do topo da pilha original
        temp = pilha.desempilhar()

        # Transfere elementos maiores de pilha_auxiliar de volta para pilha para ordenar
        while not pilha_auxiliar.esta_vazia() and pilha_auxiliar.topo() > temp:
            pilha.empilhar(pilha_auxiliar.desempilhar())

        # Coloca o elemento na posição correta em pilha_auxiliar
        pilha_auxiliar.empilhar(temp)

    # Transfere os elementos de volta para a pilha original, agora em ordem crescente
    while not pilha_auxiliar.esta_vazia():
        pilha.empilhar(pilha_auxiliar.desempilhar())

    return pilha

# Função ordenar_pilha:
# A função `ordenar_pilha` organiza os elementos da pilha em ordem crescente usando uma pilha auxiliar para ajudar na ordenação.
# 
# Passo a Passo:
# 1. Cria uma `pilha_auxiliar` que servirá para armazenar os elementos temporariamente e ordená-los.
# 2. Para cada elemento da pilha original:
#    - Remove o elemento do topo da pilha original (armazenado em `temp`).
#    - Enquanto o topo de `pilha_auxiliar` for maior que `temp`, ele será movido de volta para `pilha`, permitindo que o menor elemento fique em `pilha_auxiliar`.
#    - Depois de encontrar a posição correta, `temp` é empilhado em `pilha_auxiliar`.
# 3. Quando todos os elementos da pilha original estiverem em `pilha_auxiliar`, a ordem já estará correta.
#    - Finalmente, os elementos são transferidos de `pilha_auxiliar` de volta para `pilha`, agora na ordem crescente.
# 
# Essa abordagem tem complexidade O(n^2) devido às operações de empilhar e desempilhar necessárias para ordenar todos os elementos.

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma pilha de notas
    pilha_notas = Pilha()
    notas = [75, 85, 60, 90, 70, 80]
    
    # Adiciona as notas à pilha
    for nota in notas:
        pilha_notas.empilhar(nota)

    print("Pilha original:", pilha_notas)

    # Ordena a pilha
    ordenar_pilha(pilha_notas)

    # Exibe a pilha ordenada
    print("Pilha ordenada em ordem crescente:", pilha_notas)

# Exemplo de uso:
# Este exemplo cria uma pilha com algumas notas e as ordena em ordem crescente usando `ordenar_pilha`.
# 
# Passos:
# - A pilha `pilha_notas` é criada e preenchida com algumas notas.
# - Após a chamada de `ordenar_pilha`, a pilha é exibida para confirmar que as notas estão em ordem crescente.
# 
# Saída Esperada:
# A saída do programa deve ser algo como:
# Pilha original: [75, 85, 60, 90, 70, 80]
# Pilha ordenada em ordem crescente: [60, 70, 75, 80, 85, 90]
# 
# Isso demonstra que a função `ordenar_pilha` conseguiu orde
