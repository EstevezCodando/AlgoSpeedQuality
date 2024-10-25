from typing import List
# Funções para criar o Baralho Com cartas Embaralhadas
class Carta:
    def __init__(self, valor: int):
        self.valor = valor

    def __str__(self):
        return f"Carta({self.valor})"

class Baralho:
    def __init__(self, cartas: List[Carta]):
        self.cartas = cartas

    def embaralhar(self):
        # Embaralhar as cartas (usando um método comum de embaralhamento, como shuffle do Python)
        import random
        random.shuffle(self.cartas)

    def mostrar(self):
        # Mostrar as cartas na mão
        return [str(carta) for carta in self.cartas]


# Ordenador de cartas
class OrdenadorDeCartas:
    def __init__(self, cartas: List[Carta]):
        self.cartas = cartas

    def ordenar(self):
        for i in range(1, len(self.cartas)):
            carta_atual = self.cartas[i]
            j = i - 1
            # Movendo as cartas maiores para a frente
            while j >= 0 and self.cartas[j].valor > carta_atual.valor:
                self.cartas[j + 1] = self.cartas[j]
                j -= 1
            # Inserindo a carta no local correto
            self.cartas[j + 1] = carta_atual

        return self.cartas

def simular_ordenacao_cartas():
    # Criar as cartas de espadas (1 a 13)
    cartas_de_espadas = [Carta(valor) for valor in range(1, 14)]

    # Criar o baralho com essas cartas e embaralhar
    baralho = Baralho(cartas_de_espadas)
    baralho.embaralhar()
    print("Cartas embaralhadas:", baralho.mostrar())

    # Ordenar as cartas com a classe OrdenadorDeCartas
    ordenador = OrdenadorDeCartas(baralho.cartas)
    cartas_ordenadas = ordenador.ordenar()
    print("Cartas ordenadas:", [str(carta) for carta in cartas_ordenadas])

# Executando a simulação
if __name__ == "__main__":
    simular_ordenacao_cartas()