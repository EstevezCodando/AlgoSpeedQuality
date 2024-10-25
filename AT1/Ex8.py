#A seguinte função aceita um array de strings e retorna um novo array que contém apenas as strings que começam com o caractere "a". Use a Notação Big O para descrever a complexidade de tempo da função:


#
#

import time
import random

class ArrayOrdenavel:
    def __init__(self, array):
        self.__a = array
        self.__nItems = len(array)

    def swap(self, i, j):
        # Função para trocar dois elementos do array
        self.__a[i], self.__a[j] = self.__a[j], self.__a[i]

    def cocktailShakerSort(self):
        left = 0  # Índice à esquerda
        right = self.__nItems - 1  # Índice à direita

        # Variáveis para somar os tempos
        total_tempo_direita = 0
        total_tempo_esquerda = 0
        
        while left < right:
            # Medindo o tempo da passada da esquerda para a direita
            inicio_direita = time.time()
            
            # Passada da esquerda para a direita (levar o maior para a direita)
            for i in range(left, right):
                if self.__a[i] > self.__a[i + 1]:
                    self.swap(i, i + 1)
            
            # Reduzir o limite direito, já que o maior elemento está na posição correta
            right -= 1
            
            fim_direita = time.time()
            tempo_direita = fim_direita - inicio_direita
            total_tempo_direita += tempo_direita  # Acumulando o tempo da direita
            if tempo_direita > 0:
                print(f"Tempo da passagem esquerda para direita: {tempo_direita:.8f} segundos")
            
            # Medindo o tempo da passada da direita para a esquerda
            inicio_esquerda = time.time()
            
            # Passada da direita para a esquerda (levar o menor para a esquerda)
            for i in range(right, left, -1):
                if self.__a[i] < self.__a[i - 1]:
                    self.swap(i, i - 1)
            
            # Aumentar o limite esquerdo, já que o menor elemento está na posição correta
            left += 1
            
            fim_esquerda = time.time()
            tempo_esquerda = fim_esquerda - inicio_esquerda
            total_tempo_esquerda += tempo_esquerda  # Acumulando o tempo da esquerda
            if tempo_esquerda > 0:
                print(f"Tempo da passagem direita para esquerda: {tempo_esquerda:.8f} segundos")

        # Exibindo os tempos totais
        print(f"\nTempo total das passagens da esquerda para direita: {total_tempo_direita:.8f} segundos")
        print(f"Tempo total das passagens da direita para esquerda: {total_tempo_esquerda:.8f} segundos")

    def mostrar_array(self):
        # Função para mostrar o array atual
        return self.__a

# Exemplo de uso
if __name__ == "__main__":
    # Criando um array de 1000 elementos aleatórios
    array_exemplo = [random.randint(0, 1000) for _ in range(1000)]
    
    array_ordenavel = ArrayOrdenavel(array_exemplo)

    print("Iniciando o processo de ordenação...")
    
    # Ordenando o array com o Cocktail Shaker Sort
    array_ordenavel.cocktailShakerSort()
    
    print("Ordenação concluída.")

# A complexidade de tempo permanece O(n²) no pior caso, pois ainda temos dois loops aninhados, mas, na prática, ele pode ser um pouco mais eficiente do que o Bubble Sort clássico em certos casos.