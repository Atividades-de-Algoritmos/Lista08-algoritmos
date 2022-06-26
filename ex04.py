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
f1 = {}
for i in range(3):
  pista = input(f"informe o nome da pista[{i+1}]: ")
  voltas = []
  for j in range(4):
    voltas.append(float(input(f"informe tempo da volta[{j+1}]:")))
  f1[pista] = voltas

# e depois apresente qual a volta mais rápida em cada competição.

for i in f1.keys():
  print(f"pista: {i}, voltas: {f1[i]}, a mais rapida foi: {max(f1[i])}")