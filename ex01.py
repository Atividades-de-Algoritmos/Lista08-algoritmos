#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 1.	Em linguagem Python, faça um programa que leia um conjunto de 10 números inteiros, armazenando-o em uma
# lista (L1), calcular o quadrado dos elementos dessa lista, armazenando o resultado em oura lista (L2), imprimir todas as listas

# entrada de dados

l1 = []
for i in range(10):
  valor = int(input(f"informe o valor[{i + 1}]: "))
  l1.append(valor)

# calcular o quadrado dos elementos dessa lista, armazenando o resultado em oura lista (L2),
l2 = list(range(len(l1)))

for i in range(len(l1)):
  l2[i] = l1[i] ** 2

# imprimir todas as listas.
print(f"lista 1 = {l1}")

print("lista 2 = ", end='')
for i in range(len(l2)):
  print(l2[i], end=' ')
