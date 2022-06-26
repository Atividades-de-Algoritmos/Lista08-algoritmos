#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 1.	Em linguagem Python, faça um programa que leia um conjunto de 10 números inteiros, armazenando-o em uma
# lista (L1), calcular o quadrado dos elementos dessa lista, armazenando o resultado em oura lista (L2),
# imprimir todas as listas

# entrada de dados

l1 = [] # criar uma lista vazia
for i in range(10): # criar um laço de repetição para ler 10 valores e armazenar em uma lista
  valor = int(input(f"informe o valor[{i + 1}]: ")) # ler o valor e armazenar em uma variável
  l1.append(valor) # adicionar o valor na lista l1

# calcular o quadrado dos elementos dessa lista, armazenando o resultado em oura lista (L2),
l2 = list(range(len(l1))) # criar uma lista vazia para armazenar o resultado do quadrado dos elementos da lista l1

for i in range(len(l1)): # criar um laço para calcular o quadrado dos elementos da lista l1
  l2[i] = l1[i] ** 2 # armazenar o resultado do quadrado dos elementos da lista l1 na lista l2

# imprimir todas as listas.
print(f"lista 1 = {l1}") # imprimir a lista l1 com os valores lidos

print("lista 2 = ", end='') # imprimir a lista l2 com os valores calculados do quadrado dos elementos da lista l1
for i in range(len(l2)): # criar um laço para imprimir os valores da lista l2
  print(l2[i], end=' ') # imprimir os valores da lista l2 separados por espaço

