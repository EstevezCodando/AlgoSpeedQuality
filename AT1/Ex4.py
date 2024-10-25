def busca_binaria_com_passos(arr, elemento):
    inicio = 0
    fim = len(arr) - 1
    passos = 0  # Contador de passos

    while inicio <= fim:
        meio = (inicio + fim) // 2
        passos += 1  # Incrementa o contador de passos a cada iteração

        # Verifica se o elemento está no meio
        if arr[meio] == elemento:
            return meio, passos  # Retorna o índice do elemento e o número de passos

        # Se o elemento é maior, ignore a metade esquerda
        elif arr[meio] < elemento:
            inicio = meio + 1

        # Se o elemento é menor, ignore a metade direita
        else:
            fim = meio - 1

    return -1, passos  # Retorna -1 se o elemento não foi encontrado, e o número de passos

# Testando a função
arr = [2, 4, 6, 8, 10, 12, 13]
elemento = 8

resultado, passos = busca_binaria_com_passos(arr, elemento)

if resultado != -1:
    print(f"Elemento {elemento} encontrado no índice {resultado}.")
    print(f"Número de passos necessários: {passos}")
else:
    print(f"Elemento {elemento} não encontrado.")
    print(f"Número de passos realizados: {passos}")
