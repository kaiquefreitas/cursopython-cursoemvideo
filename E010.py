'''
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
mostre quantos dólares ela pode comprar.
'''

# importando API lib para consultar a cotação do dolar em real-time
import requests

#função p/ pegar o valor do dolar através da API Link
def get_dolar():
    link = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link) #instancinado o método requests.get 
    dict_infos = requisicao.json() #istanciando o .json e salvando no dict_infos
    valor_dolar = dict_infos['USDBRL']['bid'] #acessando o valor do dict info e atribuindo ao valor_dolar
    return valor_dolar

valor_dolar = get_dolar() #Retorno do tipo type string
valor_dolar = float(valor_dolar) # convertendo em type float

quantidade_real_usuario = float(input("Olá usuário, informe o valor em reais R$ que deseja trocar por dolar(USD)\n"))

print(f"O valor apresentado é: {quantidade_real_usuario}R$ e equivale a {(quantidade_real_usuario/valor_dolar):.2f} USD")

print("Obrigado!")
