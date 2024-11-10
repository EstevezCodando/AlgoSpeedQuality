
# Atividade 1: Implementações basicas em Estruturas de Dados e Algoritmos

### Exercício 1: Busca Linear
**Descrição:** Implementa uma busca linear para encontrar um elemento em uma lista.
**Propósito:** Demonstra o uso de busca linear e sua complexidade O(n).

### Exercício 2: Busca Binária
**Descrição:** Implementa uma busca binária em uma lista ordenada.
**Propósito:** Apresenta a eficiência da busca binária em listas ordenadas, com complexidade O(log n).

### Exercício 3: Busca Binária com Contagem de Passos
**Descrição:** A busca binária é aprimorada para contar o número de passos necessários.
**Propósito:** Demonstra o ganho de eficiência da busca binária e a quantidade de operações realizadas.

### Exercício 4: Bubble Sort Simples
**Descrição:** Implementa o algoritmo Bubble Sort básico.
**Propósito:** Explica o processo de ordenação com Bubble Sort e analisa sua complexidade quadrática.

### Exercício 5: Bubble Sort Otimizado
**Descrição:** Implementa uma versão otimizada do Bubble Sort, que verifica se a lista está ordenada a cada passagem.
**Propósito:** Mostra como pequenos ajustes podem reduzir o tempo de execução.

### Exercício 6: Ordenação de Strings
**Descrição:** Modifica o Bubble Sort para ordenar listas de strings em ordem alfabética.
**Propósito:** Expande o uso do Bubble Sort para diferentes tipos de dados.

### Exercício 7: Bubble Sort Bidirecional
**Descrição:** Implementa uma versão bidirecional do Bubble Sort, onde o maior valor é movido para a direita e o menor para a esquerda.
**Propósito:** Apresenta variações do algoritmo e seus efeitos na ordenação.

### Exercício 8: Ordenação Alfabética de Palavras em Português
**Descrição:** Ordena uma lista de palavras em português utilizando Bubble Sort.
**Propósito:** Demonstra a aplicação do Bubble Sort com dados de um idioma específico.

### Exercício 9: Análise de Complexidade Big O
**Descrição:** Implementa uma função para analisar a complexidade dos algoritmos.
**Propósito:** Mostra a importância de avaliar a complexidade do código para antecipar seu desempenho.

### Exercício 10: Contagem de Passos no Bubble Sort
**Descrição:** Conta o número de passos no Bubble Sort e compara o tempo de execução de cada passagem.
**Propósito:** Investiga a eficiência do algoritmo e quantifica a quantidade de operações.

---

## 1. Importância da organização de dados em estruturas adequadas
Organizar dados de maneira estruturada permite que o código se torne mais eficiente. Cada estrutura de dados é otimizada para determinados tipos de operações. Se você precisa, por exemplo, acessar elementos rapidamente, uma array é mais útil. Já para manipulações mais dinâmicas, uma lista ou árvore pode ser preferível. Usar a estrutura correta melhora o desempenho e economiza recursos.

## 2. Escolher a estrutura de dados com base nas operações
É importante avaliar quais operações são mais frequentes e escolher uma estrutura de dados que as suporte de forma eficiente. Por exemplo:
   - **Inserção e remoção rápidas:** listas ligadas ou filas são boas escolhas.
   - **Acesso rápido por índice:** arrays são mais eficientes.
   - **Dados ordenados e busca eficiente:** árvores binárias de busca são adequadas.
Essa análise ajuda a evitar complexidade desnecessária e a otimizar o uso de recursos.

## 3. Implementação de algoritmos eficientes
Algoritmos eficientes são essenciais para lidar com grandes volumes de dados. Um algoritmo otimizado reduz o tempo de execução e o consumo de memória, tornando o sistema mais escalável. Isso é especialmente importante em contextos onde o crescimento de dados é constante.

## 4. Algoritmo de busca linear
A busca linear percorre todos os elementos de uma lista para encontrar o valor desejado, sendo útil para listas não ordenadas. A eficiência é O(n), ou seja, o tempo cresce linearmente com o número de elementos.

```python
def busca_linear(arr, elemento):
    for i in range(len(arr)):
        if arr[i] == elemento:
            return i  # Índice encontrado
    return -1  # Não encontrado
```

## 5. Algoritmo de busca binária
Mais eficiente que a busca linear em listas ordenadas, a busca binária divide a lista em duas a cada etapa, o que resulta em uma complexidade O(log n).

```python
def busca_binaria(arr, elemento):
    inicio, fim = 0, len(arr) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == elemento:
            return meio
        elif arr[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
```

## 6. Notação Big O
A notação Big O é usada para descrever a complexidade do tempo de execução dos algoritmos:
   - **O(1):** Constante, o tempo não muda com o aumento dos dados.
   - **O(log n):** Logarítmico, comum em algoritmos de busca binária.
   - **O(n):** Linear, o tempo cresce proporcionalmente ao tamanho da entrada.
   - **O(n^2):** Quadrático, encontrado em algoritmos como o Bubble Sort.

## 7. Algoritmo de ordenação Bubble Sort
O Bubble Sort é um algoritmo simples, mas ineficiente para grandes volumes de dados. Ele compara e troca elementos adjacentes para ordená-los.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```



