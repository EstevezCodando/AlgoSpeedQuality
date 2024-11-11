class Pilha:
    def __init__(self):
        # Usamos uma lista para armazenar as tarefas, onde o último elemento representa o topo da pilha.
        self.itens = []

    def empilhar(self, item):
        """Adiciona uma nova tarefa ao topo da pilha."""
        self.itens.append(item)

    def desempilhar(self):
        """Remove e retorna a tarefa do topo da pilha."""
        return self.itens.pop() if not self.esta_vazia() else None

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0

    def topo(self):
        """Retorna a tarefa do topo da pilha sem removê-la."""
        return self.itens[-1] if not self.esta_vazia() else None

    def tamanho(self):
        """Retorna o número de tarefas na pilha."""
        return len(self.itens)

# Classe Pilha:
# A classe `Pilha` implementa uma estrutura de dados LIFO (Last In, First Out), onde a última tarefa adicionada é a primeira a ser acessada ou removida.
# Aqui, uma lista `itens` é usada para armazenar as tarefas. Cada método abaixo contribui para o funcionamento básico da pilha:
# 
# Métodos:
# - `empilhar`: Adiciona uma nova tarefa ao topo da pilha, representando a adição de uma nova tarefa no sistema.
# - `desempilhar`: Remove e retorna a tarefa do topo, simulando a execução ou conclusão da tarefa mais recente.
# - `esta_vazia`: Verifica se a pilha não contém nenhuma tarefa, útil para evitar erros ao acessar ou remover tarefas de uma pilha vazia.
# - `topo`: Retorna a tarefa do topo da pilha sem removê-la, permitindo que o sistema "espreite" a próxima tarefa a ser concluída.
# - `tamanho`: Retorna a quantidade total de tarefas na pilha, ajudando a acompanhar o número de tarefas pendentes.
# 
# A implementação com listas simplifica as operações LIFO e é suficiente para gerenciar a pilha de tarefas de forma prática e eficiente.

def tarefa_no_topo(pilha_de_tarefas):
    """
    Retorna a tarefa mais recente (no topo da pilha), sem removê-la.
    
    Parâmetros:
    pilha_de_tarefas (Pilha): A pilha de tarefas.
    
    Retorna:
    O elemento no topo da pilha, ou None se a pilha estiver vazia.
    """
    return pilha_de_tarefas.topo()

# Função tarefa_no_topo:
# A função `tarefa_no_topo` permite acessar a tarefa mais recente da pilha sem alterá-la, essencial para que o sistema mostre ao usuário
# qual é a próxima tarefa sem removê-la acidentalmente.
# 
# Parâmetros:
# - `pilha_de_tarefas`: Espera um objeto do tipo `Pilha` que representa as tarefas organizadas em ordem de chegada.
# 
# Retorno:
# - Retorna o item do topo (a tarefa mais recente) ou `None` caso a pilha esteja vazia.
# 
# Essa função é simples, mas útil para uma aplicação de gerenciamento de tarefas, pois fornece ao usuário uma visão clara da próxima tarefa.

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma pilha de tarefas
    pilha_tarefas = Pilha()
    
    # Adiciona algumas tarefas com descrições detalhadas para simular uma lista de afazeres
    pilha_tarefas.empilhar("Tarefa 1: Estudar para concurso")
    pilha_tarefas.empilhar("Tarefa 2: Comprar coisas de casa")
    pilha_tarefas.empilhar("Tarefa 3: Fazer as TP's da faculdade")
    pilha_tarefas.empilhar("Tarefa 4: Limpar a mesa de trabalho")

    # Exibe a tarefa mais recente, mostrando ao usuário a próxima ação
    tarefa_recente = tarefa_no_topo(pilha_tarefas)
    print("A tarefa mais recente é:", tarefa_recente)

# Exemplo de uso:
# Aqui, criamos uma pilha de tarefas e adicionamos algumas atividades à lista. A última tarefa adicionada representa a tarefa mais recente.
# - `empilhar`: Adiciona cada nova tarefa ao topo da pilha, seguindo a lógica de uma lista de afazeres.
# - `tarefa_no_topo`: Mostra a tarefa no topo, que deve ser a próxima tarefa a ser executada, sem removê-la da pilha.
# 
# Saída Esperada:
# O programa imprimirá:
# A tarefa mais recente é: Tarefa 4: Limpar a mesa de trabalho
# 
# Isso indica que a função `tarefa_no_topo` identificou corretamente a tarefa no topo da pilha e forneceu essa informação ao usuário.
# 
# Observação:
# A pilha continua intacta após chamar `tarefa_no_topo`, garantindo que a tarefa ainda esteja disponível para futuras visualizações ou execuções.
