#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 30/06/2022
#
# 1.	Em linguagem Python, faça um programa que leia um conjunto de 5 números inteiros, armazenando-o em uma
# lista (L1), calcular o quadrado dos elementos dessa lista, armazenando o resultado em oura lista (L2),
# Imprimir todas as listas

# Entrada de dados

l1 = [] # Criando uma lista vazia

for i in range(5): # Criando um laço de repetição para ler 5 valores e armazenar em uma lista
  valor = int(input(f"informe o valor[{i + 1}]: ")) # Solicitar um valor inteiro e armazenar em uma variável
  l1.append(valor) # Adicionando valor na lista l1 usando o .append() que coloca um item no final da lista

# Calculando o quadrado dos elementos da lista l1, armazenando os resultados em outra lista chamada (l2)
l2 = list(range(len(l1))) # Criando uma lista l2 com range() do tamanho de l1 para armazenar o resultado do quadrado dos elementos da lista l1 e fazer a comparação em um loop for.

for i in range(len(l1)): # Criar um laço para calcular o quadrado dos elementos da lista l1
  l2[i] = l1[i] ** 2 # Armazenando o resultado do quadrado dos elementos da lista l1 na lista l2

# Imprimindo todas as listas.
print(f"\nlista 1 = {l1}") # Imprimir a lista l1 com os valores lidos

print("lista 2 = ", end='') # Imprimir a lista l2 com os valores calculados do quadrado dos elementos da lista l1
for i in range(len(l2)): # Criar um laço para imprimir os valores da lista l2
  print(l2[i], end=' ') # Imprimir os valores da lista l2 separados por espaço

# Versão 2.0 do código

# ---------------------------------------------------------------------------------- #

# Entrada de dados

# l1 = [] # Criando uma lista vazia que armazena os valores informados
# l2 = [] # Criando uma lista vazia que armazena os valores informados ao quadrado

# Processamento de dados

# for x in range(5): # Laço de repetição for no range() 5, ou seja vai se repetir 5 vezes.
#  valor = int(input(f'Informe o valor {i+  1}: ')) # Solicita o valor inteiro do user.
#  l1.append(valor) # Armazenando a váriavel valor no final da lista utilizando .append()
#  valor **= 2 # Colocando o valor ao quadrado com o operador **= que é o mesmo que valor = valor ** 2
#  l2.append(valor) # Armazenando a várival valor ao quadrado no final da lista utilizando o .append()

# Saída de dados

#Imprimindo as listas
# print(f'Valores informados: {l1}') # Imprimindo a primeira lista
# print(f'Valores ao quadrado: {l2}') # Imprimindo a segunda lista

# print('fim do programa') # Informando ao user que o programa terminou

# ---------------------------------------------------------------------------------- #