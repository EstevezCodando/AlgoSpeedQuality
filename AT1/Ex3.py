
#Quantos passos seriam necessários para realizar uma busca linear pelo número 8 no array ordenado, [2, 4, 6, 8, 10, 12, 13]?

def busca_linear_com_passos(arr, elemento):
    passos = 0  # Contador de passos
    
    # Percorre cada elemento do array
    for i in range(len(arr)):
        passos += 1  # Incrementa o contador de passos
        if arr[i] == elemento:
            return i, passos  # Retorna o índice do elemento e o número de passos

    return -1, passos  # Retorna -1 se o elemento não foi encontrado

# Testando a função
arr = [2, 4, 6, 8, 10, 12, 13]
elemento = 8

resultado, passos = busca_linear_com_passos(arr, elemento)

if resultado != -1:
    print(f"Elemento {elemento} encontrado no índice {resultado}.")
    print(f"Número de passos necessários: {passos}")
else:
    print(f"Elemento {elemento} não encontrado.")
    print(f"Número de passos realizados: {passos}")
