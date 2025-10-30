def classificar_turma():
    soma_idades = 0
    num_pessoas = 0

    while True:
        try:
            idade_str = input("Digite a idade da pessoa (ou 'fim' para terminar): ")
            if idade_str.lower() == 'fim':
                break

            idade = int(idade_str)
            if idade < 0:
                print("Idade inválida. Por favor, insira um número positivo.")
                continue

            soma_idades += idade
            num_pessoas += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")
            continue

    if num_pessoas == 0:
        print("Nenhuma idade foi inserida.")
        return

    media_idade = soma_idades / num_pessoas

    print(f"\nMédia de idade da turma: {media_idade:.2f}")

    if 0 <= media_idade <= 25:
        print("A turma é jovem.")
    elif 26 <= media_idade <= 60:
        print("A turma é adulta.")
    else:  
        print("A turma é idosa.")



classificar_turma()