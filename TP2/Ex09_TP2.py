def bubble_sort(lista):
    """
    Ordena uma lista de números inteiros em ordem crescente usando o algoritmo Bubble Sort.
    
    Parâmetros:
    lista (list): Lista de números inteiros a ser ordenada.
    
    Retorna:
    list: A lista ordenada em ordem crescente.
    """
    n = len(lista)
    
    # Bubble Sort foi escolhido para ilustrar a lógica básica de um algoritmo de ordenação sem usar funções prontas.
    # Ele funciona bem para listas pequenas e demonstra a importância das trocas e comparações em uma ordenação manual.

    # Este loop externo representa cada "passagem" pela lista para garantir que todos os elementos
    # estejam na ordem correta ao final das passagens. Cada iteração leva o maior elemento não ordenado para o final.
    for i in range(n):
        # Variável de controle para verificar se houve alguma troca nesta passagem
        # Se nenhuma troca ocorrer, significa que a lista já está ordenada.
        trocou = False
        
        # Loop interno que realiza a comparação entre elementos adjacentes
        # A cada passagem, o maior elemento "sobe" para a posição correta no final da lista.
        for j in range(0, n - i - 1):
            # Compara elementos adjacentes e os troca se estiverem fora de ordem
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        # Se não houve nenhuma troca na passagem atual, a lista já está ordenada
        # Podemos interromper o loop externo para evitar iterações desnecessárias
        if not trocou:
            break
    
    # A lista já está ordenada e é retornada em ordem crescente
    return lista

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de lista de números inteiros
    lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista_exemplo)
    
    # Ordena a lista usando bubble_sort
    lista_ordenada = bubble_sort(lista_exemplo)
    print("Lista ordenada:", lista_ordenada)
