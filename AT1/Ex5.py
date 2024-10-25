#A seguinte função encontra o maior número único dentro de um array, mas tem uma eficiência de O(N²). 
# for i array:
# isValTheGreatest = true
#   for j in array:
#        if we find another value that is greater than i,
#        i is not the greatestNumber
#        if j> i:
#           isValTheGreatest = False
#       if isValTheGreatest:
#            return i


#Reescreva a função para que se torne uma eficiência O(N):

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
