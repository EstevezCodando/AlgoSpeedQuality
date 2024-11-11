class Pilha:
    def __init__(self):
        # Usamos uma lista para armazenar os elementos da pilha, que é simples e eficiente para nossas operações.
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
# A classe `Pilha` define uma estrutura LIFO (Last In, First Out), onde o último elemento adicionado é o primeiro a sair.
# Usamos uma lista para armazenar os itens, que permite as operações no topo da pilha de forma eficiente.
# 
# Métodos:
# - `empilhar`: Adiciona um elemento ao topo da pilha, simulando a adição de um novo pedido.
# - `desempilhar`: Remove e retorna o elemento no topo da pilha, se houver elementos, ou None se estiver vazia.
# - `esta_vazia`: Retorna True se a pilha não tiver nenhum elemento. Útil para verificar se podemos remover ou acessar o topo.
# - `topo`: Retorna o elemento do topo da pilha sem removê-lo, permitindo "espiar" o próximo pedido sem alterá-lo.
# - `tamanho`: Devolve a quantidade de itens na pilha, representando o número total de pedidos na estrutura.
# 
# A escolha de uma lista para a implementação é motivada pela simplicidade e pela eficiência das operações de empilhamento e desempilhamento no final da lista.

def contar_pedidos_impares(pilha_de_pedidos):
    """
    Conta a quantidade de pedidos com número de identificação ímpar na pilha.
    
    Parâmetros:
    pilha_de_pedidos (Pilha): A pilha contendo os números de identificação dos pedidos.
    
    Retorna:
    int: A quantidade de pedidos com número de identificação ímpar.
    """
    contador_impares = 0
    pilha_auxiliar = Pilha()

    # Processa cada pedido na pilha
    while not pilha_de_pedidos.esta_vazia():
        pedido = pilha_de_pedidos.desempilhar()
        
        # Verifica se o número de identificação é ímpar
        if pedido % 2 != 0:
            contador_impares += 1
        
        # Armazena o pedido na pilha auxiliar para manter a ordem original
        pilha_auxiliar.empilhar(pedido)

    # Reempilha os elementos na pilha original para manter a estrutura
    while not pilha_auxiliar.esta_vazia():
        pilha_de_pedidos.empilhar(pilha_auxiliar.desempilhar())

    return contador_impares

# Função contar_pedidos_impares:
# A função `contar_pedidos_impares` serve para contar quantos pedidos na pilha possuem números de identificação ímpares.
# Começamos criando um contador (`contador_impares`) e uma `pilha_auxiliar` para ajudar a manter a ordem original dos elementos.
# 
# Passos:
# 1. Usamos um laço `while` para desempilhar cada elemento da pilha de pedidos original e verificamos se é ímpar (usando `pedido % 2 != 0`).
#    - Se for ímpar, incrementamos `contador_impares`.
# 2. Todos os elementos são empilhados na `pilha_auxiliar` após serem verificados para que a ordem da `pilha_de_pedidos` original seja mantida.
# 3. Após o loop principal, reempilhamos todos os elementos da `pilha_auxiliar` de volta na `pilha_de_pedidos`.
# 
# Essa abordagem mantém a estrutura da pilha original e garante que a função devolva o número total de pedidos com números ímpares.
# A complexidade é \(O(n)\), já que percorremos todos os elementos, e o espaço adicional necessário é para a `pilha_auxiliar`, também \(O(n)\).

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma pilha de pedidos com identificadores variados
    pilha_pedidos = Pilha()
    
    # Adiciona alguns pedidos à pilha usando identificadores de exemplo
    pedidos = [101, 202, 303, 404, 505, 606, 707]
    for pedido in pedidos:
        pilha_pedidos.empilhar(pedido)

    # Conta e exibe a quantidade de pedidos com número de identificação ímpar
    quantidade_impares = contar_pedidos_impares(pilha_pedidos)
    print("Quantidade de pedidos com número de identificação ímpar:", quantidade_impares)

# Exemplo de uso:
# Este exemplo cria uma pilha de pedidos com alguns identificadores de exemplo para testar a função.
# Ao final, `contar_pedidos_impares` é chamada para contar quantos identificadores ímpares existem, e o resultado é exibido.
# 
# Saída esperada:
# Com os números de exemplo, esperamos que o programa mostre algo como:
# Quantidade de pedidos com número de identificação ímpar: 4
# Isso indica que 4 dos identificadores na lista são ímpares.
