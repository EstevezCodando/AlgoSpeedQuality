class TabelaHash:
    def __init__(self, tamanho):
        """
        Inicializa a tabela hash com o tamanho especificado e listas vazias em cada posição.
        
        Parâmetros:
        tamanho (int): O tamanho inicial da tabela hash.
        """
        self.tamanho = tamanho
        # Cria uma lista de listas vazias para armazenar pares de chave-valor, permitindo encadeamento para colisões
        self.tabela = [[] for _ in range(tamanho)]
    
    def _hash_func(self, chave):
        """
        Calcula o índice de uma chave na tabela usando uma função hash simples.
        
        Parâmetros:
        chave (int): A chave a ser convertida em índice.
        
        Retorna:
        int: O índice da chave na tabela.
        """
        # Utiliza o operador módulo para garantir que o índice esteja dentro dos limites da tabela
        return hash(chave) % self.tamanho
    
    def inserir(self, chave, valor):
        """
        Insere uma chave e seu valor associado na tabela hash.
        
        Parâmetros:
        chave (int): A chave do elemento.
        valor (any): O valor associado à chave.
        """
        indice = self._hash_func(chave)  # Calcula o índice usando a função hash
        # Procura se a chave já existe na lista para atualizar o valor em vez de adicionar um novo par
        for i, (chave_existente, _) in enumerate(self.tabela[indice]):
            if chave_existente == chave:
                # Atualiza o valor se a chave já existir
                self.tabela[indice][i] = (chave, valor)
                print(f"Chave {chave} atualizada com novo valor {valor}")
                return
        # Adiciona um novo par (chave, valor) se a chave não existir
        self.tabela[indice].append((chave, valor))
        print(f"Chave {chave} com valor {valor} inserida na tabela.")
    
    def buscar(self, chave):
        """
        Busca o valor associado a uma chave na tabela hash.
        
        Parâmetros:
        chave (int): A chave do elemento a ser buscado.
        
        Retorna:
        any: O valor associado à chave, ou None se a chave não for encontrada.
        """
        indice = self._hash_func(chave)  # Calcula o índice usando a função hash
        # Percorre a lista na posição calculada para encontrar a chave
        for chave_existente, valor in self.tabela[indice]:
            if chave_existente == chave:
                print(f"Chave {chave} encontrada com valor {valor}")
                return valor  # Retorna o valor associado à chave se encontrada
        print(f"Chave {chave} não encontrada na tabela.")
        return None  # Retorna None se a chave não for encontrada
    
    def remover(self, chave):
        """
        Remove uma chave e seu valor associado da tabela hash.
        
        Parâmetros:
        chave (int): A chave do elemento a ser removido.
        
        Retorna:
        bool: True se a chave foi removida com sucesso, False se a chave não foi encontrada.
        """
        indice = self._hash_func(chave)  # Calcula o índice usando a função hash
        # Percorre a lista na posição calculada para encontrar e remover a chave
        for i, (chave_existente, _) in enumerate(self.tabela[indice]):
            if chave_existente == chave:
                del self.tabela[indice][i]  # Remove o par (chave, valor) da lista
                print(f"Chave {chave} removida da tabela.")
                return True  # Retorna True para indicar que a chave foi removida
        print(f"Chave {chave} não encontrada para remoção.")
        return False  # Retorna False se a chave não for encontrada

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma tabela hash com tamanho inicial de 10
    tabela_hash = TabelaHash(10)
    
    # Insere algumas chaves e valores
    tabela_hash.inserir(1, "Jean")
    tabela_hash.inserir(2, "Michael")
    tabela_hash.inserir(12, "Estevez")  # Colisão com a chave 2 se o tamanho for 10
    
    # Busca valores associados às chaves
    tabela_hash.buscar(1)  # Deve retornar "Alice"
    tabela_hash.buscar(12) # Deve retornar "Charlie"
    tabela_hash.buscar(3)  # Deve indicar que a chave não foi encontrada
    
    # Remove uma chave e verifica se a remoção foi bem-sucedida
    tabela_hash.remover(2)  # Deve remover "Bob"
    tabela_hash.remover(3)  # Deve indicar que a chave não foi encontrada para remoção