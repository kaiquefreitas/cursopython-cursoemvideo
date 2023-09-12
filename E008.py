'''
Exercício Python 008: Escreva um programa que leia um valor em metros e 
o exiba convertido em centímetros e milímetros.
'''


def to_centimeter(medida_metro):
    centimetro = medida_metro*100
    return centimetro


def to_milimeter(medida_metro):
    milimetro = medida_metro*1000
    return milimetro


medida = float(
    input("Olá usuário, insira sua medida em metros para converter em\n cm e mm:"))

centimetro = to_centimeter(medida)
milimetro = to_milimeter(medida)

print(f"A medida em centímetro é : {centimetro:.1f} cm")

print(f"A medida em milimetro é : {milimetro:.1f} mm")
