# Escreva um código usando list comprehension em Python 
# que retorne os caracteres individuais de uma string 
# que não são caracteres de espaço em branco. 
# Aplique-a à string "Sítio do pica-pau amarelo \n 2023”.
#
#  String de exemplo
texto = "Sítio do pica-pau amarelo \n 2023"

# Inicializar uma lista vazia para armazenar os caracteres
caracteres = []

# Iterar sobre cada caractere na string
for char in texto:
    # Verificar se o caractere não é um espaço em branco
    if char != ' ':
        # Adicionar o caractere à lista
        caracteres.append(char)

# Exibindo o resultado
print(caracteres)

# Metodo 2
## String de exemplo
#texto = "Sítio do pica-pau amarelo \n 2023"

# List comprehension para obter caracteres que não são espaços em branco
#caracteres = [char for char in texto if char != ' ']

# Exibindo o resultado
#print(caracteres)
