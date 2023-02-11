import random

print('=====================================')
print('Seja Bem Vindo ao Gerador de Senha!!!')
print('=====================================')

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','y','u','v','w','x','y','z',
            '1','2','3','4','5','6','7','8','9','0',
            '!','@','#','$','%','&','*',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V']

def gera_senha(tamanho_password):
    senha = ''
    for char in range(1,tamanho_password + 1):
        senha += random.choice(chars)
    return senha

## testando script

tamanho_password = int(input('Quantos Dígitos sua senha deve conter ?'))
senha = gera_senha(tamanho_password)
print('Sua Senha é: {}'.format(str(senha)))