
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))


if num1 > num2:
    num1, num2 = num2, num1


soma = 0
numeros_intervalo = []


for numero in range(num1, num2 + 1):
    numeros_intervalo.append(numero)
    soma += numero


print(f"Números no intervalo: {numeros_intervalo}")


print(f"A soma dos números no intervalo é: {soma}")