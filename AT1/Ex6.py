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
