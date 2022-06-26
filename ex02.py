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
l1 = [] # criar uma lista vazia para armazenar os valores lidos
for i in range(6): # criar um laço de repetição para ler 6 valores e armazenar em uma lista l1
  valor = int(input(f"informe o valor[{i+1}]: ")) # ler o valor e armazenar em uma variável  valor
  l1.append(valor) # adicionar o valor na lista l1

# imprima a lista e mostre o maior elemento e a posição que ele se encontra.
print("lista = ",l1) # imprimir a lista l1 com os valores lidos com a posição de cada valor na lista l1
maior = max(l1) # armazenar o maior valor da lista l1 em uma variável maior e armazenar a posição do maior valor na lista l1

print("a posição do maior número é:" ,l1.index(maior)) # imprimir a posição do maior valor da lista l1
# ou
for i in range(len(l1)): # criar um laço para verificar se o valor da lista l1 é o maior valor da lista l1
  if l1[i] == maior: # se o valor da lista l1 for o maior valor da lista l1
    print(f"o indice do maior elemento é {i}") # imprimir o indice do maior valor da lista l1
    print(f"o maior elemento é {l1[i]}") # imprimir o maior valor da lista l1
    break # sair do laço

print("fim do programa") # imprimir a mensagem de fim do programa
