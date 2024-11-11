# ex1.py

def funcao1(n):
    """
    Função funcao1:
    Esta função realiza uma operação de print em um loop que itera de 0 até n - 1.

    Complexidade de Tempo:
    - O loop for é executado n vezes.
    - Em cada iteração, uma operação de print (complexidade O(1)) é realizada.
    - Portanto, a complexidade de tempo total é O(n), pois o loop é executado n vezes.
    """

    for i in range(n):
        print("Iteração:", i)  # O(1) por iteração


def funcao2(n):
    """
    Função funcao2:
    Esta função possui dois loops for aninhados. 
    O loop externo itera de 0 até n - 1, e para cada iteração do loop externo, o loop interno também itera n vezes.

    Complexidade de Tempo:
    - O loop externo executa n vezes.
    - Para cada iteração do loop externo, o loop interno executa n vezes.
    - Cada iteração do loop interno realiza uma operação de print com complexidade O(1).
    - Como o loop interno é executado n vezes para cada uma das n iterações do loop externo, a complexidade total é O(n * n) = O(n²).
    """

    for i in range(n):
        for j in range(n):
            print("Iteração:", i, j)  # O(1) por iteração do loop interno


def funcao3(n):
    """
    Função funcao3:
    Esta função implementa a sequência de Fibonacci de forma recursiva.

    Complexidade de Tempo:
    - Cada chamada de funcao3(n) faz duas chamadas recursivas para funcao3(n - 1) e funcao3(n - 2).
    - Isso resulta em uma árvore de chamadas exponencial.
    - A complexidade de tempo é O(2^n), pois o número de chamadas recursivas cresce exponencialmente com n.
    """

    if n <= 1:
        return n
    else:
        return funcao3(n - 1) + funcao3(n - 2)


# Exemplo de execução das funções (para teste)
if __name__ == "__main__":
    # Teste para funcao1
    print("Executando funcao1:")
    funcao1(6)

    # Teste para funcao2
    print("\nExecutando funcao2:")
    funcao2(6)

    # Teste para funcao3
    print("\nExecutando funcao3:")
    resultado = funcao3(6)
    print("Resultado de funcao3(5):", resultado)
