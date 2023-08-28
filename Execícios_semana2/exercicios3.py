# Exercícios: Listas, tuplas e dicionários. 

""" 1) Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno.
Imprima o número de alunos com média maior ou igual a 7.00. """

alunos = 10 
notas = 4 
 
medias = [] 
media_sete = 0 

 

for aluno in range(alunos):

    media = 0 

for nota in range(notas): 

    media += float(input(f"Digite a nota {nota+1} do aluno {aluno+1}: ")) 

    media /= notas 

    medias.append(media) 

    if media >= 7: 
        
        media_sete += 1 

 

print("A média dos alunos foi:") 

for aluno in range(alunos): 

    print(f"Aluno {aluno+1}: {medias[aluno]}") 
 

print(f"{media_sete} alunos tiveram média maior ou igual a 7.") 


""" 2) Programa nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome 
e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. """

nome = input("Digite o seu nome: ") 

nome_reverso = nome[::-1].upper() 

print(f"Nome ao contrário em maiúsculas:", {nome_reverso}) 


# 3) Escreva um programa em Python que onde todos os valores em um dicionário são emitidos. Se sim, imprima True. Caso contrário, imprima falso. 

dicionario = {"papagaio": "é uma ave", "refrigerante": "é uma bebida", "macarrão ao molho pesto": "é um prato", "sorvete": "é uma sobremesa"} 

todos_valores_emitidos = all(valor for valor in dicionario.values())

print(todos_valores_emitidos)


""" 4) Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:  

- "Telefonou para a vítima?" 

- "Esteve no local do crime?" 

- "Mora perto da vítima?" 

- "Devia para a vítima?" 

- "Já trabalhou com a vítima?" 

O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita"; entre 3 e 4 como "Cúmplice";
e 5 como "Assassino". Caso contrário, ela será classificada como "Inocente". """


respostas = []  # # Lista para armazenar as respostas  
 

respostas.append(input("Telefonou para a vítima? (Sim ou Não): ").lower()) 

respostas.append(input("Esteve no local do crime? (Sim ou Não): ").lower()) 

respostas.append(input("Mora perto da vítima? (Sim ou Não): ").lower()) 

respostas.append(input("Devia para a vítima? (Sim ou Não): ").lower()) 

respostas.append(input("Já trabalhou com a vítima? (Sim ou Não): ").lower()) 


positivas = respostas.count("sim") # Conta quantas respostas positivas a pessoa tem

if positivas == 2: 

    print("Classificação: Suspeita") 

elif 3 <= positivas <= 4: 

    print("Classificação: Cúmplice") 

elif positivas == 5: 

    print("Classificação: Assassino") 

else: 

    print("Classificação: Inocente") 