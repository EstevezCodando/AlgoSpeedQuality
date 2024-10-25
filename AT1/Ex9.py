# Função de Bubble Sort com prints intermediários
import random
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos já estão no lugar correto
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Printando o array a cada iteração para mostrar o processo de ordenação
        print(f"Passo {i + 1}: {arr}")
    return arr

# Testando a função com diferentes listas de números
listas_teste = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 1, 4, 2, 8],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [random.randint(0, 100) for _ in range(10)]  # Lista de 10 números aleatórios
]

# Aplicando o Bubble Sort em cada lista e exibindo o processo de ordenamento
for lista in listas_teste:
    print(f"\nOrdenando a lista: {lista}")
    bubble_sort(lista.copy())
    print("\n---\n")
