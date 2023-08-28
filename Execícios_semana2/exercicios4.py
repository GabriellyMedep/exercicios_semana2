# Exercícios: Funções 

# Faça um programa com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 

def soma(num1, num2, num3): 

    return num1 + num2 + num3 

 
 

numero1 = float(input('Digite o primeiro número: ')) 

numero2 = float(input('Digite o segundo número: ')) 

numero3 = float(input('Digite o terceiro número: ')) 

 
 

resultado = soma(numero1, numero2, numero3) 

print(f"A soma dos três números é: {resultado}") 


# 2) Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Ex: 127 -> 721 

def reverso_numero(numero): 

    numero_str = str(numero) 

    reverso_str = numero_str[::-1] 

    reverso = int(reverso_str) 

    return reverso 

 
 

numero = int(input("Digite um número inteiro: ")) 

reverso = reverso_numero(numero) 

print(f"O reverso do número {numero} é: {reverso}") 


""" 3) Escreva um script que pergunte ao usuário se ele deseja converter em temperatura de graus celsius para fahrenheit ou vice-versa. 
Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, 
onde esse menu chama a função de conversão correta. """

def celsius_para_fahrenheit(celsius): 

    fahrenheit = (celsius * 9/5) + 32 

    return fahrenheit 

 

def fahrenheit_para_celsius(fahrenheit): 

    celsius = (fahrenheit - 32) * 5/9 

    return celsius 


def menu(): 

    print("Escolha uma opção:") 

    print("1. Converter de Celsius para Fahrenheit") 

    print("2. Converter de Fahrenheit para Celsius") 

    opcao = int(input("Digite o número da opção desejada: ")) 

     

    if opcao == 1: 

        celsius = float(input("Digite a temperatura em Celsius: ")) 

        fahrenheit = celsius_para_fahrenheit(celsius) 

        print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F") 

        return 

    elif opcao == 2: 

        fahrenheit = float(input("Digite a temperatura em Fahrenheit: ")) 

        celsius = fahrenheit_para_celsius(fahrenheit) 

        print(f"{fahrenheit:.2f}°F é igual a {celsius:.2f}°C") 

        return 

    else: 

        print("Opção inválida") 

menu() 

# 