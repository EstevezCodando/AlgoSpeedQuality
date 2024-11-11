# ex1_map.py

from collections import defaultdict

class StepCounter:
    def __init__(self):
        self.steps = 0

    def increment(self, count=1):
        self.steps += count

    def reset(self):
        self.steps = 0

    def get_steps(self):
        return self.steps


class Algoritmos:
    @staticmethod
    def funcao1(n, step_counter):
        for i in range(n):
            step_counter.increment()

    @staticmethod
    def funcao2(n, step_counter):
        for i in range(n):
            for j in range(n):
                step_counter.increment()

    @staticmethod
    def funcao3(n, step_counter):
        step_counter.increment()
        if n <= 1:
            return n
        else:
            return Algoritmos.funcao3(n - 1, step_counter) + Algoritmos.funcao3(n - 2, step_counter)


def armazenar_passos(algoritmo):
    step_map = defaultdict(int)
    for entrada in range(1, 21):
        step_counter = StepCounter()
        algoritmo(entrada, step_counter)
        step_map[entrada] = step_counter.get_steps()
    return step_map


# Função principal para armazenar os dados das funções
if __name__ == "__main__":
    passos_funcao1 = armazenar_passos(Algoritmos.funcao1)
    passos_funcao2 = armazenar_passos(Algoritmos.funcao2)
    passos_funcao3 = armazenar_passos(Algoritmos.funcao3)

    print("Passos para funcao1:", dict(passos_funcao1))
    print("Passos para funcao2:", dict(passos_funcao2))
    print("Passos para funcao3:", dict(passos_funcao3))
