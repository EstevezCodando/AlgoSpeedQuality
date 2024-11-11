class Pilha:
    def __init__(self):
        # Usamos uma lista simples para armazenar os elementos da pilha,
        # pois as operações de adicionar e remover no topo são eficientes em listas.
        self.itens = []

    def empilhar(self, item):
        """Adiciona um novo pedido ao topo da pilha."""
        self.itens.append(item)

    def desempilhar(self):
        """Remove e retorna o pedido do topo da pilha."""
        return self.itens.pop() if not self.esta_vazia() else None

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0

    def topo(self):
        """Retorna o pedido do topo da pilha sem removê-lo."""
        return self.itens[-1] if not self.esta_vazia() else None

    def tamanho(self):
        """Retorna o número de pedidos na pilha."""
        return len(self.itens)

# Classe Pilha:
# Essa classe define uma estrutura básica de pilha, onde o último elemento a ser adicionado é o primeiro a ser removido (LIFO - Last In, First Out).
# Aqui usamos uma lista para armazenar os elementos, aproveitando o fato de que o `append` e o `pop` são operações rápidas no final da lista.
# 
# Métodos:
# - `empilhar`: Adiciona um novo elemento (pedido) ao topo da pilha.
# - `desempilhar`: Remove e retorna o elemento no topo da pilha, se a pilha não estiver vazia.
# - `esta_vazia`: Retorna True se a pilha estiver vazia, o que é útil para verificações antes de remover ou acessar elementos.
# - `topo`: Retorna o elemento no topo da pilha sem removê-lo, útil para obter o pedido mais recente sem afetar a estrutura.
# - `tamanho`: Devolve a quantidade total de elementos na pilha.
# 
# Escolhemos uma lista para a estrutura da pilha pois é simples e eficiente para os métodos LIFO (inserção e remoção no final). Essa classe ajuda a organizar
# pedidos de forma que o último a entrar é o primeiro a sair, simulando bem a estrutura de uma pilha.

def contar_pedidos_pares(pilha_de_pedidos):
    """
    Conta a quantidade de pedidos com número de identificação par na pilha.
    
    Parâmetros:
    pilha_de_pedidos (Pilha): A pilha contendo os números de identificação dos pedidos.
    
    Retorna:
    int: A quantidade de pedidos com número de identificação par.
    """
    contador_pares = 0
    pilha_auxiliar = Pilha()

    # Processa cada pedido na pilha
    while not pilha_de_pedidos.esta_vazia():
        pedido = pilha_de_pedidos.desempilhar()
        
        # Verifica se o número de identificação é par
        if pedido % 2 == 0:
            contador_pares += 1
        
        # Armazena o pedido na pilha auxiliar para manter a ordem original
        pilha_auxiliar.empilhar(pedido)

    # Reempilha os elementos na pilha original para manter a estrutura
    while not pilha_auxiliar.esta_vazia():
        pilha_de_pedidos.empilhar(pilha_auxiliar.desempilhar())

    return contador_pares

# Função contar_pedidos_pares:
# Essa função serve para contar os pedidos com números pares de identificação na pilha. 
# Para isso, usamos um contador `contador_pares` que é incrementado toda vez que encontramos um número par.
# 
# Como estamos desempilhando cada elemento para verificar, a ordem da pilha seria modificada. Para evitar isso, usamos uma `pilha_auxiliar`.
# Depois de verificar e contar, transferimos os pedidos de volta da `pilha_auxiliar` para a `pilha_de_pedidos`.
# 
# Essa abordagem garante que a estrutura da pilha permaneça a mesma ao final da execução, e a função retorna a quantidade total de pedidos com números pares.
# 
# Complexidade:
# - A função é linear, \(O(n)\), já que precisa percorrer todos os elementos da pilha.
# - Em termos de espaço, precisamos de uma pilha auxiliar, então também é \(O(n)\).

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma pilha de pedidos
    pilha_pedidos = Pilha()
    
    # Adiciona alguns números de identificação dos pedidos à pilha
    pedidos = [101, 202, 303, 404, 505, 606, 707]
    for pedido in pedidos:
        pilha_pedidos.empilhar(pedido)

    # Conta e exibe a quantidade de pedidos com número de identificação par
    quantidade_pares = contar_pedidos_pares(pilha_pedidos)
    print("Quantidade de pedidos com número de identificação par:", quantidade_pares)

# Exemplo de uso:
# No exemplo acima, criamos uma pilha de pedidos e adicionamos alguns números de identificação.
# A função contar_pedidos_pares é chamada para contar quantos desses números são pares, e o resultado é exibido no console.
# Esse exemplo ajuda a visualizar a função em uma situação prática e permite verificar se a contagem está funcionando corretamente.
# 
# Esperamos que o programa exiba algo como:
# Quantidade de pedidos com número de identificação par: 3
# Onde a contagem de pares está de acordo com a lista de números adicionados.
