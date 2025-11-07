def mensagem(aluno, idade, curso):
  print(f"O aluno {aluno}, tem {idade} anos e cursa {curso}")


alunos = [{"nome": "Pedro", "idade": 23, "curso" : "ADS"},
          {"nome": "Miguel", "idade": 20, "curso" : "ADS"},
          {"nome": "Daniel", "idade": 27, "curso" : "ADS"},
          {"nome": "Maria", "idade": 60, "curso" : "ENG"},
          {"nome": "Clara", "idade": 20, "curso" : "ADS"},
          {"nome": "Eduarda", "idade": 20, "curso" : "ADS"},
          {"nome": "Lucas", "idade": 19, "curso" : "Tecnico"},
          {"nome": "Marcos", "idade": 18, "curso" : "ADS"}]

while True:
  nome = input("Digite o nome, ou 'sair' para sair:")
  if nome.upper() == "SAIR":
    break
  idade = int(input("Digite a idade:"))
  curso = input("Digite o curso:")

  alunos.append({"nome": nome, "idade": idade, "curso": curso})

for aluno in alunos:
  mensagem(aluno["nome"], aluno["idade"], aluno["curso"])