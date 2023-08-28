# Exercício Conceitos Básicos de Python

# 1) Faça um Programa que peça um número e então mostre a mensagem: -> O número informado foi [número].  

numero = int(input('digite um numero: ')) 

print(f' o número digitado foi {numero}') 


# 2) Faça um programa que peça dois números e imprima a soma. 

numero1 = int(input('Digite o numero 1: ')) 

numero2 = int(input('Digite o numero 2: ')) 

soma = numero1 + numero2 

print(soma) 


# 3) Faça um programa que peça a temperatura em graus Celsius, transformando em graus Fahrenheit. 

celsius = float(input("Digite a temperatura em graus Celsius: ")) 

# convertendo para Fahrenheit 

fahrenheit = celsius * 9/5 + 32 

print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.") 


""" 4) Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês. """

valor_por_hora = float(input("Digite o valor que você ganha por hora: ")) 

horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: ")) 

salario_total = valor_por_hora * horas_trabalhadas 

print(f"Seu salário total no mês é: R$ {salario_total:.2f}") 