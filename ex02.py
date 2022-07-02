#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 30/06/2022
#
# 2. Em linguagem Python, faça um programa que leia 6 valores e os armazene em uma lista,
# imprima a lista e mostre o maior elemento e a posição que ele se encontra.

# Entrada de dados

l1 = [] # Criando uma lista vazia para armazenar os valores lidos
for i in range(6): # Criando um laço de repetição para ler 6 valores e armazenar em uma lista l1.
  valor = int(input(f"Informe o valor[{i+1}]: ")) # Solicitar um valor inteiro do user
  l1.append(valor) # Adicionando valor na lista l1

# Processamento e saída de dados

print("\nlista = ", l1) # Imprimindo a lista l1

maior = max(l1) # Armazenando o maior valor da lista l1 em uma variável chamada maior utilizando a função max()

print(f'O maior elemento de l1 é', maior) # Imprimindo o maior elemento da lista l1
print("A posição do maior elemento de l1 é:" , l1.index(maior) + 1) # Imprimindo a posição (Indíce) do maior valor da lista l1 utilizando o método .index() que me vai me retornar um valor int.


# Versão 2.0 do código

# ---------------------------------------------------------------------------------- #

# Entrada de dados (mesma do anterior)

# Processamento e saída de dados

# print("lista = ",l1) # Imprimindo a lista l1

# maior = max(l1) # Armazenando o maior valor da lista l1 em uma variável chamada maior utilizando a função max()

# for i in range(len(l1)): # Criando loop para verificar se um valor da lista l1 é igual maior valor da lista l1
  
  # if l1[i] == maior: # Se o valor da lista l1 for igual ao maior valor da lista l1 executa a identação
    # print(f"O indíce do maior elemento é {i}") # Imprimindo o indíce do maior valor da lista l1
    # print(f"O maior elemento é {l1[i]}") # Imprimindo o maior valor da lista l1
    # break # Saindo do laço de repetição for

# ---------------------------------------------------------------------------------- #

print("\nfim do programa") # Informando ao user que o programa terminou
