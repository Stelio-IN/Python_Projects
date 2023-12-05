import random

#Possibilitar rodar o jogo nX
while True:
    #array de escolhas
    escolhas = ["pedra","papel","tesoura"]
    #pegando de forma aletoria as escolhas para o computador
    computer = random.choice(escolhas)

    #enquanto a escolha do player nao for iual a da lista fica repetindo
    player = None
    while player not in escolhas:
        player = input("pedra, papel ou tesoura?: ").lower()

    # if player==computer:
    #     print("Computer: ",computer)
    #     print("player: ",player)
    #     print("Tie")
    # elif player == "pedra":
    #     if computer == "papel":
    #         print("Computer: ", computer)
    #         print("player: ", player)
    #         print("You lose!!! :(")
    #     if computer == "tesoura":
    #         print("Computer: ", computer)
    #         print("player: ", player)
    #         print("you win!!! :)")
    # elif player == "papel":
    #     if computer == "tesoura":
    #         print("Computer: ", computer)
    #         print("player: ", player)
    #         print("You lose!!! :(")
    #     if computer == "pedra":
    #         print("Computer: ", computer)
    #         print("player: ", player)
    #         print("you win!!! :)")
    # elif player == "tesoura":
    #     if computer == "pedra":
    #         print("Computer: ", computer)
    #         print("player: ", player)
    #         print("You lose!!! :(")
    #     if computer == "papel":
    #         print("Computer: ", computer)
    #         print("player: ", player)
    #         print("you win!!! :)")
    #
    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie")
    #Agrupando todas a opcoes de vitoria reduzindo assim o codigo
    #Podia fazer o inverso agrupar todos casos de derrota before um else para vitoria
    elif (player == "pedra" and computer == "tesoura") or (player == "papel" and computer == "pedra") or (
            player == "tesoura" and computer == "papel"):
        print("Computer: ", computer)
        print("Player: ", player)
        print("You win!!! :)")
    else:
        print("Computer: ", computer)
        print("Player: ", player)
        print("You lose!!! :(")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Closing")
