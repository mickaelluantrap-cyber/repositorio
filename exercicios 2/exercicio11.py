salario = float(input("Digite o valor do seu salario bruto"))

pct_aumento = 0

if salario > 0 and salario < 1450:
    pct_aumento = 20
elif salario < 2800:
     pct_aumento = 15
elif salario <= 3500:
     pct_aumento = 10
else:
     pct_aumento = 5

val_aumento = salario * (pct_aumento/100)

novo_salario = salario + val_aumento


