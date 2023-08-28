# Exercícios extras de python 

""" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. 
Considere a tabela de conversão abaixo:  

Dólar americano: R$ 4,91 

Peso argentino: R$ 0,02 

Dólar australiano: R$ 3,18 

Dólar canadense: R$ R$ 3,64 

Franco suíço: R$ 0,42 

Euro: R$ 5,36 

Libra esterlina: R$ 6,21  """

def converter_para_moeda(valor_em_reais, taxa): 

    valor_em_moeda = valor_em_reais / taxa 

    return valor_em_moeda 
 

valor_em_reais = float(input("Digite o valor em reais que você tem na carteira: ")) 


taxas_de_conversao = { 

    "Dólar americano": 4.91, 

    "Peso argentino": 0.02, 

    "Dólar australiano": 3.18, 

    "Dólar canadense": 3.64, 

    "Franco suíço": 0.42, 

    "Euro": 5.36, 

    "Libra esterlina": 6.21 
} 


print("Valores que você poderia comprar em outras moedas:") 

for moeda, taxa in taxas_de_conversao.items(): 

    valor_convertido = converter_para_moeda(valor_em_reais, taxa) 

    print(f"{moeda}: {valor_convertido:.2f}") 


""" 2) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$80,00 por dia e R$0,20 por km rodado. """

def preco_aluguel(km_percorridos, dias_alugados): 

    preco_por_dia = 80.00 

    preco_por_km = 0.20 

    preco_total = (preco_por_dia * dias_alugados) + (preco_por_km * km_percorridos) 

    return preco_total 
 

km_percorridos = float(input("Digite a quantidade de km percorridos: ")) 

dias_alugados = int(input("Digite a quantidade de dias alugados: ")) 


preco_total = preco_aluguel(km_percorridos, dias_alugados) 

print(f"O preço a pagar pelo aluguel é: R$ {preco_total:.2f}") 


""" 3) Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. 

Se o salário for até R$ 1000,00 o funcionário terá 20% de aumento. 

Entre R$ 1001,00 até R$ 2800,00 o funcionário terá 10% de aumento. 

Acima de R$ 2801,00 o funcionário terá 5% de aumento. """


salario = float(input("Digite o salário do funcionário: ")) 

if salario <= 1000.00: 

    aumento_percentual = 0.20 

elif salario <= 2800.00: 

    aumento_percentual = 0.10 

else: 

    aumento_percentual = 0.05 


aumento = salario * aumento_percentual 

novo_salario = salario + aumento 

 
print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}") 


""" 4) Crie um programa que tenha a função leiaInt (), que vai funcionar de forma semelhante à função input () do python, 
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n’) """

def leiaInt(mensagem): 

    while True: 

        try: 

            valor = int(input(mensagem)) 

            return valor 

        except ValueError: 

            print("Valor inválido. Digite um valor numérico inteiro.") 
 

n = leiaInt('Digite um número inteiro: ') 

print(f'Você digitou o número: {n}') 

