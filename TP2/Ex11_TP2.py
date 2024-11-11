from collections import deque

class FilaAtendimento:
    def __init__(self):
        # Inicializa a fila usando deque, que permite adição e remoção eficientes em ambos os extremos.
        self.fila = deque()

    def adicionar_cliente(self, nome):
        """
        Adiciona um cliente ao final da fila.
        
        Parâmetros:
        nome (str): O nome do cliente a ser adicionado à fila.
        """
        self.fila.append(nome)  # Adiciona o nome do cliente ao final da fila
        print(f"Cliente {nome} foi adicionado à fila.")

    def atender_cliente(self):
        """
        Remove o cliente do início da fila para atendimento e exibe o nome do cliente.
        
        Retorna:
        str: O nome do cliente que está sendo atendido ou uma mensagem se a fila estiver vazia.
        """
        if self.tamanho_fila() > 0:
            # Remove e retorna o cliente no início da fila
            cliente = self.fila.popleft()
            print(f"Atendendo o cliente: {cliente}")
            return cliente
        else:
            # Retorna uma mensagem se não houver clientes na fila
            print("A fila está vazia. Nenhum cliente para atender.")
            return None

    def tamanho_fila(self):
        """
        Retorna o número de clientes restantes na fila.
        
        Retorna:
        int: A quantidade de clientes na fila.
        """
        # Retorna o tamanho da fila usando len()
        return len(self.fila)

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma instância de FilaAtendimento
    fila_atendimento = FilaAtendimento()
    
    # Adiciona clientes à fila
    fila_atendimento.adicionar_cliente("Jean")
    fila_atendimento.adicionar_cliente("Michael")
    fila_atendimento.adicionar_cliente("Alvarez")
    
    # Exibe o tamanho da fila antes do atendimento
    print("Tamanho da fila:", fila_atendimento.tamanho_fila())
    
    # Atende clientes na ordem de chegada
    fila_atendimento.atender_cliente()
    fila_atendimento.atender_cliente()
    
    # Exibe o tamanho da fila após alguns atendimentos
    print("Tamanho da fila:", fila_atendimento.tamanho_fila())
    
    # Atende o próximo cliente e verifica se há clientes restantes
    fila_atendimento.atender_cliente()
    fila_atendimento.atender_cliente()  # Tenta atender um cliente quando a fila está vazia
