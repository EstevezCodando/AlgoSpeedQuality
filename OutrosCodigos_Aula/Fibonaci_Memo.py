def fibonacci(n, memo={}, contador=None):
    """
    Calcula o n-ésimo número da sequência de Fibonacci usando memoização e conta os passos necessários.
    
    Parâmetros:
    n (int): A posição desejada na sequência de Fibonacci (n >= 0).
    memo (dict): Dicionário para armazenar resultados de chamadas anteriores para otimizar o cálculo.
    contador (dict): Dicionário com uma chave 'passos' para contar o número de operações.
    
    Retorna:
    int: O n-ésimo número de Fibonacci.
    """
    # Inicializa o contador na primeira chamada
    if contador is not None:
        contador['passos'] += 1  # Conta este passo

    # Caso base: Fibonacci(0) = 0, Fibonacci(1) = 1
    if n <= 1:
        return n

    # Verifica se o valor já foi calculado e armazenado em memo
    if n not in memo:
        # Calcula e armazena o resultado no dicionário memo
        memo[n] = fibonacci(n - 1, memo, contador) + fibonacci(n - 2, memo, contador)
    
    # Retorna o valor armazenado para Fibonacci(n)
    return memo[n]

# Loop para aceitar entradas de diferentes valores de n e reutilizar o dicionário memo
def main():
    memo = {}  # Inicializa o dicionário memo fora do loop para reutilizar valores já calculados

    print("Calculadora de Fibonacci com Memoização")
    print("Digite um número para calcular o Fibonacci ou 'sair' para terminar.")
    
    while True:
        # Solicita a entrada do usuário
        entrada = input("Digite um valor para n: ")
        
        # Verifica se o usuário quer sair do programa
        if entrada.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        try:
            # Converte a entrada para um inteiro
            n = int(entrada)
            
            # Garante que o valor de n é não negativo
            if n < 0:
                print("Por favor, insira um número inteiro não negativo.")
                continue
            
            # Inicializa o contador de passos
            contador = {'passos': 0}
            
            # Calcula o n-ésimo número de Fibonacci e obtém o número de passos
            resultado = fibonacci(n, memo, contador)
            print(f"Número de passos para calcular Fibonacci({n}): {contador['passos']}")
            print(f"Fibonacci({n}) = {resultado}")
        
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro ou 'sair'.")

if __name__ == "__main__":
    main()