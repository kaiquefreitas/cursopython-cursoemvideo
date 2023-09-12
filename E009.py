'''
Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e 
mostre na tela a sua tabuada.
'''

numero_tabuada = int(input("Olá usuário, insira um número para saber sua tabuada:\n"))

print("=="*10)
for i in range (1,11):
    print(f"{numero_tabuada} x {i} = {i*numero_tabuada}\n")
print("=="*10)
