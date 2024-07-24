import random
def jogar_adivinhação():
    num = random.randint(1,100)
    numu = None
    tent = 0 

    while numu != num:
        try:
            numu = int(input("Digite um número entre 1 e 100: "))
            tent += 1
            if numu < num:
                print("\nNúmero digitado é baixo\n")
            elif numu > num:
                print("\nNúmero digitado é alto\n")
            else:
                print("\nParabens acertou o número!")
        except ValueError:
            print("Por favor, digite um numero válido\n")

    print('\nNúmero de tentativas: {}'.format(tent))


while True:
    #Mensagem de boas vindas
    print('                        BEM VINDO AO JOGO: ADIVINHE O NÚMERO!                   ')
    print("Manual do jogo: Será gerado um número aleatório entre 1 e 100.")
    print("Você terá que acertar esse número com a menor quantidade de tentativas possível. Boa sorte!")
    print('-'*20)

    jogar_adivinhação()


    jogar_novamente = input('\nDeseja jogar novamente? s/n: ').strip().lower()

    while jogar_novamente not in ('s', 'n'):
        input("Resposta inválida, digite uma resposta válida: ")


    if jogar_novamente == 'n':
        break

input("\nPressione enter para sair")




