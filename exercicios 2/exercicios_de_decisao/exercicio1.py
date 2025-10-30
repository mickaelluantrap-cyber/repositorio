nota = float(input("Digite o valor da nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida, digite uma nota entre 0 e 10")
    nota = float(input("Digite o valor da nota: "))

    print(f"Você digitou a nota {nota}, que é um valor válido")

