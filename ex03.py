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

agenda = dict()  # criar um dicionário vazio para armazenar os contatos
for i in range(3): # criar um laço de repetição para ler 3 contatos e armazenar em um dicionário agenda
  nome = input(f"informe o nome do contato[{i+1}]: ") # ler o nome do contato e armazenar em uma variável nome
  fones = [] # criar uma lista vazia para armazenar os números de telefone do contato nome
  while True: # criar um laço para ler os números de telefone do contato nome e armazenar em uma lista fones
    fones.append(input("informe um número de fone: ")) # ler um número de telefone e armazenar em uma lista fones e adicionar na lista fones
    valor = input("deseja informar outro número? (S/n)") # ler se deseja informar outro número de telefone e armazenar em uma variável valor
    if valor != 'S': # se a variável valor não for igual a 'S'
      break # sair do laço e continuar o programa
  agenda[nome] = fones # adicionar o nome do contato e os números de telefone do contato nome no dicionário agenda e armazenar na chave nome e os valores da lista fones

# Depois, crie uma estrutura de repetição para listar todos os contados da agenda.
for i,y in agenda.items(): # criar um laço para listar os contatos da agenda e armazenar em uma variável i e em uma variável y
  print(f"nome: {i} -> número(s): {y}") # imprimir o nome do contato e os números de telefone do contato nome na lista fones

print("fim do programa") # imprimir a mensagem de fim do programa