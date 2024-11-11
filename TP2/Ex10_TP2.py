from collections import deque

def contar_livros_impares(fila_livros):
    """
    Conta quantos livros possuem um número de identificação ímpar na fila.
    
    Parâmetros:
    fila_livros (deque): Uma fila contendo os números de identificação dos livros.
    
    Retorna:
    int: O número total de livros com números de identificação ímpares.
    """
    # Inicializa o contador de identificações ímpares
    contador_impares = 0  
    
    # Itera sobre cada livro na fila de livros
    for livro_id in fila_livros:
        # Verifica se o número de identificação é ímpar
        # Um número é ímpar se o resto da divisão por 2 é diferente de zero
        if livro_id % 2 != 0:
            contador_impares += 1  # Incrementa o contador se o número for ímpar
    
    # Retorna o número total de livros com identificação ímpar
    return contador_impares  

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma fila de livros usando deque, onde cada número representa um ID de livro
    fila_livros = deque([101, 202, 303, 404, 505, 606, 707])
    
    # Conta a quantidade de livros com números de identificação ímpares
    quantidade_impares = contar_livros_impares(fila_livros)
    
    # Exibe o resultado para o usuário
    print("Quantidade de livros com números de identificação ímpares:", quantidade_impares)
