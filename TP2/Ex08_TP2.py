from collections import deque

class Fila:
    def __init__(self):
        # Usamos deque para representar a fila, pois é eficiente para operações de enfileiramento e desenfileiramento
        self.itens = deque()

    def enfileirar(self, item):
        """Adiciona um paciente ao final da fila."""
        self.itens.append(item)

    def desenfileirar(self):
        """Remove e retorna o paciente no início da fila."""
        return self.itens.popleft() if not self.esta_vazia() else None

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0

    def tamanho(self):
        """Retorna o número de pacientes na fila."""
        return len(self.itens)

    def __str__(self):
        """Representação da fila para impressão."""
        return str(list(self.itens))

# Classe Fila:
# A ideia aqui foi usar uma deque (doble-ended queue) como base para implementar a fila, pois
# esse tipo de estrutura é otimizado para adicionar e remover elementos nas extremidades.
# Esse uso é particularmente eficiente para operações que precisamos na clínica.
# A classe inclui métodos básicos:
# - `enfileirar`: Para adicionar um paciente no final da fila.
# - `desenfileirar`: Remove o primeiro paciente (seguindo a ordem de chegada).
# - `esta_vazia`: Retorna True se a fila estiver vazia.
# - `tamanho`: Devolve o número de pacientes na fila.
# - `__str__`: Permite imprimir a fila de forma mais amigável.
# 
# No geral, essa classe encapsula bem as operações básicas de uma fila e facilita a manipulação da ordem dos pacientes.

def inverter_fila(fila):
    """
    Inverte a ordem dos elementos da fila.
    
    Parâmetros:
    fila (Fila): A fila de pacientes em ordem de chegada.
    
    Retorna:
    Fila: A fila com a ordem dos elementos invertida.
    """
    pilha_temporaria = []

    # Aqui, transferimos todos os elementos da fila para uma pilha temporária.
    # Ao fazer isso, estamos invertendo a ordem dos pacientes (último entra primeiro).
    while not fila.esta_vazia():
        pilha_temporaria.append(fila.desenfileirar())

    # Em seguida, transferimos os elementos da pilha de volta para a fila.
    # Isso reordena a fila para que o último paciente agora seja o primeiro.
    while pilha_temporaria:
        fila.enfileirar(pilha_temporaria.pop())

    return fila

# Função inverter_fila:
# A ideia aqui é aproveitar a natureza LIFO (Last In, First Out) da pilha.
# Primeiro, pegamos todos os pacientes da fila e empilhamos na pilha_temporaria.
# Como a pilha opera ao contrário, isso automaticamente inverte a ordem.
# Depois, "desempilhamos" e recolocamos os pacientes na fila.
# Com isso, o primeiro paciente da fila original passa a ser o último e vice-versa.
# 
# Essa abordagem é eficiente para nossa necessidade, pois requer apenas duas transferências entre
# estruturas, mantendo a complexidade linear O(n).

# Exemplo de uso
if __name__ == "__main__":
    # Criando a fila de pacientes com alguns exemplos de nomes
    fila_pacientes = Fila()
    pacientes = ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 4", "Paciente 5"]

    # Adicionando pacientes na fila conforme a ordem de chegada
    for paciente in pacientes:
        fila_pacientes.enfileirar(paciente)

    print("Fila original:", fila_pacientes)

    # Invertendo a fila e mostrando o resultado
    fila_invertida = inverter_fila(fila_pacientes)
    print("Fila invertida:", fila_invertida)

# Exemplo de uso:
# Criamos uma fila de pacientes com alguns exemplos para testar o código.
# - Primeiro, exibimos a fila original para ver a ordem de chegada.
# - Em seguida, aplicamos a função inverter_fila e exibimos a fila invertida.
# 
# Esse exemplo é útil para ver a função funcionando em uma situação prática.
# A função inverter_fila deveria transformar uma lista como ["Paciente 1", "Paciente 2", "Paciente 3"]
# em ["Paciente 3", "Paciente 2", "Paciente 1"], facilitando o atendimento em ordem inversa.

# Saída esperada:
# O programa imprimirá:
# Fila original: ['Paciente 1', 'Paciente 2', 'Paciente 3', 'Paciente 4', 'Paciente 5']
# Fila invertida: ['Paciente 5', 'Paciente 4', 'Paciente 3', 'Paciente 2', 'Paciente 1']
