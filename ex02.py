#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 2.	Em linguagem Python, faça um programa que leia 6 valores e os armazene em uma lista,
# imprima a lista e mostre o maior elemento e a posição que ele se encontra.


# entrada de dados

# faça um programa que leia 6 valores e os armazene em uma lista,
l1 = []
for i in range(6):
  valor = int(input(f"informe o valor[{i+1}]: "))
  l1.append(valor)

# imprima a lista e mostre o maior elemento e a posição que ele se encontra.
print("lista = ",l1)
maior = max(l1)

print("a posição do maior número é:" ,l1.index(maior))
# ou
for i in range(len(l1)):
  if l1[i] == maior:
    print(f"o indice do maior elemento é {i}")