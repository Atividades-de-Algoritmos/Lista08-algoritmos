#
#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# Data: 30/06/2022
#
#
# 3 - Em linguagem Python, faça um programa que crie uma agenda de telefones (3 contatos) que seja um
# dicionário para armazenar o nome (chave) e armazene os números de telefones (elemento), cada pessoa pode
# ter 1 ou mais números de telefones, fazendo a leitura dos valores por meio de uma estrutura de repetição.
# Depois, crie uma estrutura de repetição para listar todos os contados da agenda.

# Entrada de dados

agenda = dict() # Criando um dicionário vazio para armazenar os contatos

# Processamento de dados

for i in range(3): # Criando um laço de repetição para ler 3 contatos e armazenar em um dicionário agenda
  nome = input(f"\nInforme o nome do contato[{i+1}]: ") # Solicitando o nome do contato
  fones = [] # Criando uma lista vazia para armazenar os números de telefone do contato
  
  while True: # Criando um laço para ler os números de telefone do contato nome e armazenar em uma lista fones
    fones.append(input("Informe um número de fone: ")) # Solicitando um número de telefone e armazenando no final da lista fones usando o .append()
    valor = input(f"\n{nome} tem outro número? (s/n)") # Solicitando se deseja informar outro número de telefone
    
    if valor.lower() != 's': # Se a variável valor não for igual a 's' executa a identação, .lower() método que joga todos caracteres pra minúsculo, ou seja, se o user digitar com S maíusculo o programa ainda vai rodar.
      break # Saindo do laço com o break
  
  agenda[nome] = fones # Adicionando o nome do contato e os números de telefone do contato nome no dicionário agenda e armazenar na chave nome e os valores da lista fones

# Saída de dados

print('\nContatos Disponíveis\n') # Imprimindo mensagem no terminal

for c, e in agenda.items(): # Criando um laço para listar os contatos da agenda
  print(f"Nome: {c} | número(s): {e}") # Imprimindo o nome do contato e os números

print("\nfim do programa") # Informando ao user que o programa terminou