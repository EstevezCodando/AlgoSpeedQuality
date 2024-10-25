def greatestNumber(array):
    if not array:  # Verifica se o array não está vazio
        return None  # Retorna None se o array for vazio

    # Inicializa o maior número como o primeiro elemento do array
    maior = array[0]
    
    # Percorre o array uma única vez
    for i in array:
        if i > maior:
            maior = i  # Atualiza o maior número
    
    return maior

# Testando a função
arr = [2, 4, 6, 8, 10, 12, 13]
resultado = greatestNumber(arr)
print(f"O maior número é: {resultado}")
