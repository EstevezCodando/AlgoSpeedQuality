def bubble_sort_strings_pt(arr):
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Comparação direta
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr

# Testando a função com diferentes listas de strings em português
listas_teste_strings_pt = [
    ["Carlos", "Ana", "Maria", "Clara"],
    ["zebra", "elefante", "cão", "gato", "pássaro"],
    ["laranja", "uva", "maçã", "banana"],
    ["maçã", "banana", "cereja"],
    ["kiwi", "kiwi", "uva", "melão", "maçã"]
]

# Aplicando o Bubble Sort em cada lista de strings e exibindo o resultado
resultados_strings_pt = [bubble_sort_strings_pt(lista.copy()) for lista in listas_teste_strings_pt]
print(resultados_strings_pt)
