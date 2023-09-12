'''
Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
'''

note_one = float(input("Olá usuário, insira a primeira nota do aluno:\n"))
note_two = float(input("Agora insira a segunda nota do aluno:\n"))

print(f"A média aritmética do aluno é: {(note_one+note_two)/2:.1f}")
