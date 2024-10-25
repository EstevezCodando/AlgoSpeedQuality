import inspect

def analisar_complexidade(func):
    # Obter o código fonte da função como uma string
    codigo_fonte = inspect.getsource(func)
    
    # Contar quantos loops existem no código (for e while)
    loops = codigo_fonte.count('for') + codigo_fonte.count('while')
    
    # Verificar se há uma redução do espaço de busca (busca binária, por exemplo)
    if 'inicio <= fim' in codigo_fonte and '// 2' in codigo_fonte:
        return "O(log n) - Tempo logarítmico (provável busca binária)"
    
    # Se houver loops, verificamos o tipo de complexidade
    if loops == 0:
        return "O(1) - Tempo constante"
    elif loops == 1:
        return "O(n) - Tempo linear"
    elif loops == 2:
        return "O(n^2) - Tempo quadrático"
    else:
        return f"O(n^{loops}) - Tempo polinomial (com {loops} loops)"


# Função exemplo fornecida
def selectAStrings(array):
    newArray = []

    for i in range(len(array)):
        if array[i].startswith("a"):
            newArray.append(array[i])

    return newArray


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

    return -1, passos  # Retorna -1 se o elemento não foi encontrado


# Usando a função para analisar a complexidade da função selectAStrings
complexidade = analisar_complexidade(busca_binaria_com_passos)
print(f"Complexidade estimada: {complexidade}")
complexidade = analisar_complexidade(selectAStrings)
print(f"Complexidade estimada: {complexidade}")
