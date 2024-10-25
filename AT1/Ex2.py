#Pegue um baralho de cartas: retire as 13 cartas de espadas, reserve o resto e embaralhe as cartas de espadas. Elabore um algoritmo para ordená-las por número sob as seguintes restrições:
# Todas as cartas devem ser seguradas em uma mão. Esta é a "primeira" mão.
# Inicialmente, as cartas embaralhadas estão todas empilhadas com as faces em uma direção, de modo que apenas uma carta seja visível.
# Inicialmente, todas as cartas são seguradas entre o polegar e o indicador da primeira mão.
# A carta visível na pilha pode ser retirada usando a outra mão e colocada entre quaisquer dedos da primeira mão. Ela só pode ser colocada na frente ou atrás das cartas na pilha de cartas entre esses dedos.
# A outra mão pode segurar apenas uma carta por vez e deve colocá-la em algum lugar na primeira mão antes de pegar outra carta visível de uma das pilhas.
# O algoritmo termina quando todas as cartas estão ordenadas em uma única pilha na mão.



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