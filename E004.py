'''
Exercício Python 004: Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

entrada = input("Insira um valor\n")

print("O valor inserido é do tipo:", type(entrada))

print("O valor inserido é do tipo numérico? ", entrada.isnumeric())
print("O valor inserido é do tipo texto? ", entrada.isalpha())
print("O valor inserido é do tipo alfanúmerico? ", entrada.isalnum())
print("O valor inserido é do tipo digit string? ", entrada.isdigit())
print("O valor inserido é do tipo decimmal? ", entrada.isdecimal())
print("O valor inserido é do tipo 'printável'? ", entrada.isprintable())
