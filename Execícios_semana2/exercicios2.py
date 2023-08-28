# Exercícios: Tomada de Decisão e Estruturas de Repetição. 

# 1) Faça um programa que peça dois números e imprima o maior deles. 

numero1 = int(input('Digite o primeiro numero: ')) 

numero2 = int(input('Digite o segundo numero: ')) 

if numero1 > numero2: 

    maior_numero = numero1 

else: 

    maior_numero = numero2 

print("o maior número é:", maior_numero) 


""" 2) Faça um programa que imprima o turno em que você estuda. Peça para digitar M – matutino ou V – vespertino ou N – noturno. 
Imprima a mensagem “bom dia”, “boa tarde”, “boa noite” ou “valor inválido”, conforme o caso. """

turno = input('digite seu turno, m – matutino ou v – vespertino ou n – noturno: ') 

if turno == "m": 

    print("bom dia") 

elif turno == "v": 

    print("boa tarde") 

elif turno == "n": 

    print("boa noite") 

else:  

    print('Valor inválido.') 


""" 3) Faça um programa que peça uma nota, entre 0 e 10.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. """

nota = -1 

while nota < 0 or nota > 10: 

    nota = int(input("Digite uma nota entre 0 e 10: ")) 

if nota <0 or nota > 10: 

     print("valor inválido. Tente novamente") 



