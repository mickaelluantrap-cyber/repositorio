limite_peso = 50
multa_kg = 4.000

peso_pescado = float(input("Quantos kg de peixe você pescou? "))

execedente = peso_pescado - limite_peso

valor_multa = execedente * multa_kg

print(f"O execedente é {execedente}kg e o valor da multa é RS:{valor_multa}")

