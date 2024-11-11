#A seguinte função aceita um array de strings e retorna um novo array que contém apenas as strings que começam com o caractere "a". 

# Função fornecida
def selectAStrings(array):
    newArray = []

    for i in range(len(array)):
        if array[i].startswith("a"):
            newArray.append(array[i])

    return newArray


## Use a Notação Big O para descrever a complexidade de tempo da função:

#A complexidade de tempo dessa função é O(n), 
# pois o tempo de execução está crescendo linearmente com o tamanho do array de strings.

#for i in range(len(array))
# Este loop itera sobre todos os elementos do array. 
# Portanto, se o array tiver n elementos, ele será executado n vezes.

#----------------------#
# array[i].startswith("a")
#Para cada string no array, a função startswith() verifica se a string começa com a letra "a".
# A complexidade de startswith() é O(k), 
# onde k é o comprimento da string, 
# pois ele percorre os primeiros caracteres da string para verificar o prefixo. 
# No entanto, como estamos verificando apenas o primeiro caractere,
# podemos considerar isso O(1), ou seja, constante.