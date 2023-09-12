'''
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

largura = float(input('Informe a largura da parede em m (metros)\n'))
altura = float(input("Informe altura da parede em m (metros)\n"))

print(f'A área total da parede é: {(largura*altura):.2f}m²')
print(f'A quantidade de tinta necessária para pintá-la é: {(largura*altura/2):.2f} L')