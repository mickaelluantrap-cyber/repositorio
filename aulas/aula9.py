laço de repetição

servem para repetir certo trecho de codigo até que uma condição seja satisfeita

o laço while serve para ser executado enquanto uma condiçao for true ,caso a condição passe a ser
false ele encerra a execução do progama. usado especificamente quando não sabemos quantas execuções são nessesarias


while condição     | while valor !=5:
 #código           | valor = int(input("tentativa: "))
 #repetido         | if valor !=5
                   | print("errou!")
                   | print("Acertou")

 o laço for serve para situações que sabemos a quantidade de repetições.
 Podemos iterar entre um array ou entre valores com um contador

for item in vetor:          for contador in range(i,f,p):
#código a                    #código a repetir
#repetir

 alunos = ["Ana","Camili","Evilyn"]    

