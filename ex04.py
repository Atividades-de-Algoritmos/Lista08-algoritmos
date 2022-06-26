#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
#
# 4.	Em linguagem Python, escreva um programa que leia os tempos de 4 voltas (elemento) na pista em 3
# competições (chave) de um piloto de F-1, em seguida apresente a média dos tempos das voltas nas 3 competições,
# e depois apresente qual a volta mais rápida em cada competição.

# entrada de dados
# escreva um programa que leia os tempos de 4 voltas (elemento) na pista em 3 competições (chave) de um piloto de F-1,

f1 = {} # criar um dicionário vazio para armazenar os tempos de cada volta em cada competição de F-1
for i in range(3): # criar um laço de repetição para ler 3 competições de F-1 e armazenar em um dicionário f1 os tempos de cada volta
  pista = input(f"informe o nome da pista[{i+1}]: ") # ler o nome da pista e armazenar em uma variável pista e adicionar na chave pista
  voltas = [] # criar uma lista vazia para armazenar os tempos de cada volta da pista pista e adicionar na chave voltas
  for j in range(4): # criar um laço de repetição para ler os tempos de cada volta da pista pista e armazenar em uma lista voltas
    voltas.append(float(input(f"informe tempo da volta[{j+1}]:"))) # ler o tempo de cada volta da pista pista e armazenar em uma lista voltas e adicionar na lista voltas
  f1[pista] = voltas # adicionar a pista pista e os tempos de cada volta da pista pista no dicionário f1 e armazenar na chave pista e os valores da lista voltas

# e depois apresente qual a volta mais rápida em cada competição.

for i in f1.keys(): # criar um laço para listar as competições de F-1 e armazenar em uma variável i os nomes das competições
  print(f"pista: {i}, voltas: {f1[i]}, a mais rapida foi: {max(f1[i])}") # imprimir o nome da pista e os tempos de cada volta da pista i e a volta mais rapida da pista i
  # ou
  # print(f"pista: {i}, voltas: {f1[i]}, a mais rapida foi: {f1[i].index(max(f1[i]))+1}") # imprimir o nome da pista e os tempos de cada volta da pista i e a volta mais rapida da pista i
#
# print("fim do programa") # imprimir a mensagem de fim do programa
