import random

def encontrar_duplicados_forca_bruta(lista):
    """
    Encontra números duplicados em uma lista usando uma abordagem de força bruta.
    
    Parâmetros:
    lista (list): A lista de elementos a ser verificada.
    
    Retorna:
    list: Uma lista contendo os elementos duplicados encontrados.
    """
    duplicados = []
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

def encontrar_duplicados_otimizado(lista):
    """
    Encontra números duplicados em uma lista usando um conjunto para otimizar a busca.
    
    Parâmetros:
    lista (list): A lista de elementos a ser verificada.
    
    Retorna:
    list: Uma lista contendo os elementos duplicados encontrados.
    """
    vistos = set()
    duplicados = set()
    for elemento in lista:
        if elemento in vistos:
            duplicados.add(elemento)
        else:
            vistos.add(elemento)
    return list(duplicados)

# Exemplo de uso
if __name__ == "__main__":
    # Gerar uma lista de 1 milhão de números aleatórios entre 1 e 500.000 para garantir alguns duplicados
    lista_teste = [random.randint(1, 500000) for _ in range(1000000)]
    
    # Encontrar duplicados usando força bruta (ineficiente para listas grandes)
    print("Duplicados encontrados (força bruta):")
    duplicados_forca_bruta = encontrar_duplicados_forca_bruta(lista_teste[:1000])  # Usamos apenas 1000 elementos para a força bruta
    print(duplicados_forca_bruta)
    
    # Encontrar duplicados usando o método otimizado com set
    print("Duplicados encontrados (otimizado):")
    duplicados_otimizado = encontrar_duplicados_otimizado(lista_teste)
    print(duplicados_otimizado)
