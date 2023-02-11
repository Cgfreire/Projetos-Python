from ast import If
import math
import time

print("**************************************************")
print("Bem vindo a calculadora de Funções do Segundo Grau")
print("************************************************** \n")

nome_usuario = input("Digite seu nome:")

print(f"\nA função dessa calculadora é ajudar você {nome_usuario} a encontrar os valores de X nas equações de Segundo Grau")

print("Para isso vou precisar que você informe os valores de a, b e c:")
valor_a = int(input("Digite o valor de a: "))
valor_b = int(input("Digite o valor de b: "))
valor_c = int(input("Digite o valor de c: "))

if(valor_b == 0):
    valor_delta = float(-valor_c / valor_a)
    raiz_delta = math.sqrt(valor_delta)
    x1 = +raiz_delta
    x2 = -raiz_delta
else:
    valor_delta = float((valor_b * valor_b) - 4 * valor_a * valor_c)
    raiz_delta = math.sqrt(valor_delta)

    x1 = (-valor_b + raiz_delta) / (2 * valor_a)
    x2 = (-valor_b - raiz_delta) / (2 * valor_a)

for i in range(3):
    print("Calculando...")
    time.sleep(2)

print("Resultado encontrado!!!")
print(f"O valor de x' é: {x1}")
print(f"O valor de x'' é: {x2}")