print("M - Matutino | V - Vespertino | N - Noturno")
turno = input("Digite a letra correspondente ao turno: ")

if turno == "M" or turno == "m":
    print("bom dia")
elif turno == "V" or turno == "v":
 print("boa tarde")
elif turno == "N" or turno == "n":
 print("boa noite")

else:
    print("Valor errado")
