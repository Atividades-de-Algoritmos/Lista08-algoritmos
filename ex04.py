#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 30/06/2022
#
#
# 4 - Em linguagem Python, escreva um programa que leia os tempos de 4 voltas (elemento) na pista em 3
# competições (chave) de um piloto de F-1, em seguida apresente a média dos tempos das voltas nas 3 competições e depois apresente qual a volta mais rápida em cada competição.

# Entrada de dados

f1 = {} # Criando um dicionário vazio para armazenar os tempos de cada volta em cada competição de F-1

for p in range(3): # Criando um laço de repetição para ler 3 competições de F-1 e armazenar em um dicionário f1 os tempos de cada volta.
  pista = input(f"\nInforme o nome da pista[{p + 1}]: ") # Solicitando o nome da pista
  voltas = [] # Criando uma lista vazia para armazenar os tempos de cada volta da pista
  
  for v in range(4): # Criando um laço para ler os tempos de cada volta da pista
    voltas.append(float(input(f"Informe tempo da volta[{v + 1}]:"))) # lendo o tempo de volta da pista e armazenando no final da lista voltas
  
  f1[pista] = voltas # Adicionando a pista e os tempos de cada volta da pista no dicionário f1 e armazenando na chave pista os valores da lista voltas

# Processamento e saída de dados


# Imprimindo quais foram as voltas e qual a mais rápida em cada competição

for c in f1.keys(): # Criando um laço para listar as competições de F-1
  print(f"\nPista: {c}, Voltas: {f1[c]}, Melhor volta: {min(f1[c])}, Média: {sum(f1[c]) / len(f1[c])}") # Imprimido o nome da pista, suas voltas, qual foi a melhor volta e a média.

print("\nfim do programa") # Informando ao user que o programa terminou
