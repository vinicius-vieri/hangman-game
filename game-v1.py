import random 
from os import system, name

#funcao para limpeza de tela
def limpar():
    #windows
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def jogo():

    limpar()
    print("Bem vindo ao jogo da forca!")
    print("Este jogo serve para experienciar minhas habilidades básicas com python")

    # podemos criar a lista aqui mesmo
    """# temas
    paises = ["brasil", "dinamarca", "portugal", "chile", "china",
               "peru", "holanda", "catar", "egito", "espanha", "gibraltar",
               "guiana", "haiti", "israel", "mali", "nepal", "paraguai", "vaticano"]
    
    animais = ["galo", "bode", "vaca", "girafa", "galinha", "arara", "pato", "lagarto", "aranha",
               "peru", "cachorro", "camelo", "golfinho", "zebra", "touro", "centopeia"]
    
    objetos = ["canivete", "perfume", "notebook", "porta", "chaves", "cama", "ventilador", "cadeira",
               "mesa", "estojo", "tapete", "toalha", "chinelo", "sapato"] """
    
    # ou podemos abrir os arquivos que torna tudo mais interessante
    paises = open("hangmanGame/paises.txt", "r").read().splitlines()
    animais = open("hangmanGame/animais.txt", "r").read().splitlines()
    objetos = open("hangmanGame/objetos.txt", "r").read().splitlines()

    
    tema = int(input("Escolha um tema\n 1 - paises\n 2 - animais\n 3 - objetos\nDigite um valor: "))

    # tratamento de erro para escolha de tema
    while True:
        if tema == 1:
            tema = paises
            break
        elif tema == 2:
            tema = animais
            break
        elif tema == 3:
            tema = objetos
            break
        else:
            print("Você digitou um valor inválido, por favor tente novamente")
            tema = int(input("Digite um valor: "))


    # aleatorizando
    palavra = random.choice(tema)

    # colocando "_"
    letras_descobertas = ["_" for letra in palavra]

    chances = 10

    letras_erradas = []

    # loop enquanto ainda restarem chances
    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("\nLetras erradas:", " ".join(letras_erradas))

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print("Voce venceu, a palavra era: ", palavra)
            break
    
    if "_" in letras_descobertas:
        print("Voce perdeu, a palavra era: ", palavra)



# main do python
if __name__ == "__main__":
    jogo()

