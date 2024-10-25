#Imagine que você tem um tabuleiro de xadrez e coloca um único grão de arroz em um quadrado. No segundo quadrado, você coloca 2 grãos de arroz, já que isso é o dobro da quantidade de arroz no quadrado anterior. No terceiro quadrado, você coloca 4 grãos. No quarto quadrado, você coloca 8 grãos, e no quinto quadrado, você coloca 16 grãos, e assim por diante.
#
#   Escreva a função em python que calcula em qual quadrado do tabuleiro você precisará colocar uma determinada quantidade de grãos de arroz. 
# Por exemplo, para 16 grãos, a função retornará 5, já que você colocará os 16 grãos no quinto quadrado.


def encontrar_quadrado(grains):
    quadrado = 1
    graos_no_quadrado = 1  # No primeiro quadrado, há 1 grão
    
    while graos_no_quadrado < grains:
        quadrado += 1
        graos_no_quadrado *= 2  # Dobra o número de grãos a cada quadrado
    
    return quadrado

# Testando a função
grains = 16
resultado = encontrar_quadrado(grains)
print(f"A quantidade de {grains} grãos será colocada no quadrado {resultado}.")


# Use a Notação Big O para descrever a complexidade de tempo da função que você acabou de criar.
#A complexidade de tempo da função é O(log N), onde N é o número de grãos. 
# Isso ocorre porque o número de grãos cresce exponencialmente, e a cada iteração estamos dobrando o número de grãos. 
# Assim, a quantidade de quadrados a serem percorridos é proporcional ao logaritmo da quantidade de grãos.

#Especificamente, a complexidade é O(log N), base 2, porque estamos dobrando o número de grãos a cada quadrado.