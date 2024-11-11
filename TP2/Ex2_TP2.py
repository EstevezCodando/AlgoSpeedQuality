import random
import math

def merge_sort(lista):
    """
    Função de ordenação Merge Sort.
    Este algoritmo é do tipo "dividir e conquistar" e possui uma complexidade de tempo de O(n log n).
    Ele é eficiente para grandes listas e é um dos algoritmos de ordenação mais usados em situações que requerem boa performance.
    
    Parâmetros:
    lista (list): A lista de elementos a ser ordenada.
    
    Retorna:
    list: Uma nova lista com os elementos ordenados.
    """
    # Se a lista tiver apenas um elemento ou estiver vazia, já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Encontrar o ponto médio da lista
    meio = len(lista) // 2
    
    # Dividir a lista em duas partes
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Ordenar recursivamente as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    # Mesclar as duas metades ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    """
    Função auxiliar para mesclar duas listas ordenadas.
    Compara elementos das duas listas e os mescla em ordem crescente.
    
    Parâmetros:
    esquerda (list): Primeira lista ordenada.
    direita (list): Segunda lista ordenada.
    
    Retorna:
    list: Uma nova lista contendo os elementos das duas listas em ordem crescente.
    """
    resultado = []
    i = j = 0
    
    # Comparar elementos e mesclar em ordem
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adicionar os elementos restantes (se houver) das duas listas
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

def print_list_partial(lista, max_elements=20):
    """
    Função auxiliar para imprimir um subconjunto de elementos da lista para validação.
    
    Parâmetros:
    lista (list): A lista a ser impressa.
    max_elements (int): O número máximo de elementos a serem exibidos.
    """
    print("Primeiros elementos da lista ordenada:", lista[:max_elements])
    if len(lista) > max_elements:
        print("... ({} elementos no total)".format(len(lista)))

# Exemplo de uso
if __name__ == "__main__":
    # Gerar uma lista de 2000 números aleatórios
    lista_teste = [random.randint(1, 5000000) for _ in range(2000)]
    
    # Ordena a lista usando merge_sort
    lista_ordenada = merge_sort(lista_teste)
    
    # Exibe os primeiros 20 elementos da lista ordenada para verificar
    print("A lista original de 2000 elementos foi ordenada.")
    print_list_partial(lista_ordenada)
