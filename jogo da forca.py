import random


def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia",
                "logica", "programacao", "tendencias"]
    palavra = random.choice(palavras)
    return palavra


def exibir_forca(tentativas):
    estagios = [
        '''
           -----
           |   |
               |
               |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        '''
    ]
    print(estagios[tentativas])


def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    tentativas_maximas = 6
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print(" ".join(palavra_oculta))

    while tentativas < tentativas_maximas and "_" in palavra_oculta:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1

        exibir_forca(tentativas)
        print(" ".join(palavra_oculta))
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")

        if "_" not in palavra_oculta:
            print("Parabéns, você venceu! A palavra era:", palavra)
            break
    else:
        if tentativas == tentativas_maximas:
            print("Você perdeu! A palavra era:", palavra)

    print("Obrigado por jogar!")
    input("Pressione Enter para sair...")


# Iniciar o jogo
jogar()
