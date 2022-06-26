#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
#
# 3.	Em linguagem Python, faça um programa que crie uma agenda de telefones (3 contatos) que seja um
# dicionário para armazenar o nome (chave) e armazene os números de telefones (elemento), cada pessoa pode
# ter 1 ou mais números de telefones, fazendo a leitura dos valores por meio de uma estrutura de repetição.
# Depois, crie uma estrutura de repetição para listar todos os contados da agenda.

# entrada de dados:
# faça um programa que crie uma agenda de telefones (3 contatos) que seja um dicionário para armazenar
# o nome (chave) e armazene os números de telefones (elemento), cada pessoa pode ter 1 ou mais números de
# telefones, fazendo a leitura dos valores por meio de uma estrutura de repetição.
agenda = dict()
for i in range(3):
  nome = input(f"informe o nome do contato[{i+1}]: ")
  fones = []
  while True:
    fones.append(input("informe um número de fone: "))
    valor = input("deseja informar outro número? (S/n)")
    if valor != 'S':
      break
  agenda[nome] = fones

# Depois, crie uma estrutura de repetição para listar todos os contados da agenda.
for i,y in agenda.items():
  print(f"nome: {i} -> número(s): {y}")