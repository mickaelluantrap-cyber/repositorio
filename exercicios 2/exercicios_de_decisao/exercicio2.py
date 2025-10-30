nome = input("Digite seu nome: ")
while len(nome) < 3:
    print(f"Nome invalido, ele precisa ter mais de 3 caracteres")
nome = input("Digite o seu nome: ")

idade = int(input("Digite a sua idade: "))
while idade <0 or idade > 150:
    print(f"Idade invalida , ela precisa ser entre 0 a 150")
idade = float(input("Digite sua idade"))

salario = float(input("Digite o seu salario: "))
while salario < 0:
print(f"salario invalida , ela precisa ser maior que 0")
salario = float(input("Digite seu salario: "))
print("S - solteiro | C - Casad | V - Viuvo | D - Divorciado")
estado_sivil = input("Digite seu estado civil:").lower()
while estad



