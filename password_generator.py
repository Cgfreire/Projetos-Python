import random

print('=====================================')
print('Seja Bem Vindo ao Gerador de Senha!!!')
print('=====================================')

chars = 1,2,3,4,5,6,7,8,9,0
senha = []
i = 0

def gera_senha(tamanho_password):
    while(i > tamanho_password):
        senha = senha.append(random.choice(chars))

        

## testando script

tamanho_password = int(input('Quantos Dígitos sua senha deve conter ?'))
gera_senha(tamanho_password)
print('Sua Senha é: {}'.format(str(senha)))