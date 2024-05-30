#import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#numeros = int(input('Digite um numero: '))
#numeros_2 = int(input('Digite outro numero: '))

#print(numeros + numeros_2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#num = int(input('Digite um número: '))
#calculo_resto = num % 5
#print(calculo_resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#number_1 = int(input('Primeiro número: '))
#number_2 = int(input('Segundo número: '))
#resultado = number_1 * number_2
#print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#numero_01 = int(input("Inserir um numero inteiro: "))
#numero_02 = int(input("Inserir outro numero inteiro: "))
#resultado = numero_01 // numero_02
#print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#number_3 = int(input('Digite um número para trazer quadrático: '))
#resultado = number_3 ** 2
#print(resultado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#number_4 = float(input('Digite o primeiro número: '))
#number_5 = float(input('Digite o segundo número: '))
#resultado = number_4 + number_5
#print(resultado)


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#number_6 = float(input('Digite um numero: '))
#number_7 = float(input('Digite outro numero: '))
#resultado = (number_6 + number_7) / 2
#print(resultado)


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#number_8 = float(input('Digite a base: '))
#number_9 = float(input('Digite o expoente: '))
#resultado = number_8 ** number_9
#print(f"{resultado:.2f}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#celsius = 30
#conversao = celsius * 1.8 + 32
#print(conversao)

# celsius = float(input("Digite a temperatura em Celsius: "))
#celsius = 30.0  # Exemplo de entrada
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#name_1 = input('Digite seu nome: ')
#print(name_1.upper())


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#name_2 = input('Digite seu nome completo: ')
#print(name_2.lower())


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#frase = input('Digite uma frase: ')
#texto = frase.strip()
#print(texto)


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
#lista_de_dia_mes_ano = data_do_usuario.split("/")
#print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
#print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
#print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#name_3 = input('Digite seu primeiro nome: ')
#name_4 = input('Digite seu sobrenome: ')
#nome_concatenado = name_3 + " " + name_4
#print(nome_concatenado)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#interrogacao_1 = True
#interrogacao_2 = False
#resultado = interrogacao_1 and interrogacao_2
#print(resultado)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#interrogacao_3 = False
#interrogacao_4 = True
#resultado = interrogacao_3 or interrogacao_4
#print(resultado)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#digitacao = bool(input("Digite um boleano: "))
#digitacao_null = not digitacao
#print(digitacao)


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#numero_dig = int(input('Digite um numero: '))
#numero_2dig = int(input('digite outro numero: '))
#resultado = numero_dig == numero_2dig
#print(resultado)


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#numero_dig3 = int(input('Digite o terceiro numero: '))
#numero_dig4 = int(input('Digite o quarto numero: '))
#resultado = numero_dig3 != numero_dig4
#print(resultado)


# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação