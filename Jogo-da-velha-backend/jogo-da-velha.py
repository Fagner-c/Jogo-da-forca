from os import system
from random import choice
from time import sleep
def titulo(t):
    print('='*20, t, '='*20)
lista_palavras = {
                'comida' : ['arroz carreteiro', 'feijoada', 'coxinha', 'moqueca de peixe', 'acarajé', 'baião de dois', 'pão de queijo', 'pamonha', 'carne de sol'],
                'esporte' : ['futebol', 'basquete', 'críquete', 'rúgbi', 'beisebol'],
                'profissão' : ['engenharia de pesca', 'gestão ambiental', 'fonoaudiologia', 'analise e desenvolvimento de sistemas']}
letra_usuario = []
letras_especiais = {'u' :['ú', 'ù', 'û'],
                    'i' : ['í', 'ì', 'î'],
                    'o' : ['ò', 'ó', 'õ', 'ô'],
                    'e' : ['é', 'è', 'ê'],
                    'c' : ['ç'],
                    'a' : ['á', 'à', 'â', 'ã']}
conta_vitorias = 0
conta_derrotas = 0
while True:
    system('cls')
    titulo('INICIO')
    inicio = str(input('Deseja jogar [s/n]: ')).lower()
    system('cls')
    if inicio == 'sim' or inicio == 's':
        while True:
            letra_usuario = []
            system('cls')
            titulo('SELEÇÃO DO TEMA')
            print('Escolha o tema da palavra ')
            print('[1]Comida\n[2]Esporte\n[3]Profissão\n[4]Sair')
            opc = str(input('Informe o tema: '))
            match opc:
                case '1':
                    palavra = choice(lista_palavras['comida'])
                    cont = 0
                    jogador = ''
                    for letra in palavra:
                        if letra == ' ':
                            jogador +=' '
                        else:
                            jogador += '-'
                    while True:
                        if jogador == palavra:
                            system('cls')
                            print('Você ganhou!')
                            conta_vitorias += 1
                            print(f'Você jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}')
                            sleep(2)
                            break
                        elif cont == 6:
                            system('cls')
                            print('Você perdeu!')
                            conta_derrotas += 1
                            print(f'Você jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}')
                            sleep(2)
                            break
                        else:
                            system('cls')
                            titulo('COMIDA')
                            print(jogador)
                            print('Letra já digitadas: ', end='')
                            for p in letra_usuario:
                                print(p ,end=' ')
                            newpalavra =''
                            letra_do_jogador = str(input('\nEscolha uma letra: '))
                            if len(letra_do_jogador) == 1:
                                if letra_do_jogador not in letra_usuario:
                                    if letra_do_jogador in letras_especiais.keys():
                                        for letra in palavra:
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                    letra_usuario.append(letra_do_jogador)
                                    if(letra_do_jogador in palavra):
                                        for letra in palavra:
                                            if letra in letra_usuario:
                                                newpalavra += letra
                                            elif letra == ' ':
                                                newpalavra +=' '
                                            else:
                                                newpalavra += '-'  
                                        jogador = newpalavra                                        
                                    else:
                                        system('cls')
                                        print(f'Letra não pertence a palavra! \nVocê ainda tem {5-cont} chances')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                else:
                                    print('A letra já foi digitada antes, tente novamente!')
                                    sleep(2)
                            else:
                                system('cls')
                                print('Digite apenas uma letra!')
                                sleep(2)
                case '2':
                    palavra = choice(lista_palavras['esporte'])
                    cont = 0
                    jogador = ''
                    for letra in palavra:
                        if letra == ' ':
                            jogador +=' '
                        else:
                            jogador += '-'
                    while True:
                        if jogador == palavra:
                            system('cls')
                            print('Você ganhou!')
                            conta_vitorias += 1
                            print(f'Você jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}')
                            sleep(2)
                            break
                        elif cont == 6:
                            system('cls')
                            print('Você perdeu!')
                            conta_derrotas += 1
                            print(f'Você jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}')
                            sleep(2)
                            break
                        else:
                            system('cls')
                            titulo('COMIDA')
                            print(jogador)
                            print('Letra já digitadas: ', end='')
                            for p in letra_usuario:
                                print(p ,end=' ')
                            newpalavra =''
                            letra_do_jogador = str(input('\nEscolha uma letra: '))
                            if len(letra_do_jogador) == 1:
                                if letra_do_jogador not in letra_usuario:
                                    if letra_do_jogador in letras_especiais.keys():
                                        for letra in palavra:
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                    letra_usuario.append(letra_do_jogador)
                                    if(letra_do_jogador in palavra):
                                        for letra in palavra:
                                            if letra in letra_usuario:
                                                newpalavra += letra
                                            elif letra == ' ':
                                                newpalavra +=' '
                                            else:
                                                newpalavra += '-'  
                                        jogador = newpalavra                                        
                                    else:
                                        system('cls')
                                        print(f'Letra não pertence a palavra! \nVocê ainda tem {5-cont} chances')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                else:
                                    print('A letra já foi digitada antes, tente novamente!')
                                    sleep(2)
                            else:
                                system('cls')
                                print('Digite apenas uma letra!')
                                sleep(2)
                case '3':
                    palavra = choice(lista_palavras['profissão'])
                    cont = 0
                    jogador = ''
                    for letra in palavra:
                        if letra == ' ':
                            jogador +=' '
                        else:
                            jogador += '-'
                    while True:
                        if jogador == palavra:
                            system('cls')
                            print('Você ganhou!')
                            conta_vitorias += 1
                            print(f'Você jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}')
                            sleep(2)
                            break
                        elif cont == 6:
                            system('cls')
                            print('Você perdeu!')
                            conta_derrotas += 1
                            print(f'Você jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}')
                            sleep(2)
                            break
                        else:
                            system('cls')
                            titulo('COMIDA')
                            print(jogador)
                            print('Letra já digitadas: ', end='')
                            for p in letra_usuario:
                                print(p ,end=' ')
                            newpalavra =''
                            letra_do_jogador = str(input('\nEscolha uma letra: '))
                            if len(letra_do_jogador) == 1:
                                if letra_do_jogador not in letra_usuario:
                                    if letra_do_jogador in letras_especiais.keys():
                                        for letra in palavra:
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                    letra_usuario.append(letra_do_jogador)
                                    if(letra_do_jogador in palavra):
                                        for letra in palavra:
                                            if letra in letra_usuario:
                                                newpalavra += letra
                                            elif letra == ' ':
                                                newpalavra +=' '
                                            else:
                                                newpalavra += '-'  
                                        jogador = newpalavra                                        
                                    else:
                                        system('cls')
                                        print(f'Letra não pertence a palavra! \nVocê ainda tem {5-cont} chances')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                else:
                                    print('A letra já foi digitada antes, tente novamente!')
                                    sleep(2)
                            else:
                                system('cls')
                                print('Digite apenas uma letra!')
                                sleep(2)
                case '4': 
                    break
    elif inicio == 'não' or  inicio == 'n' or inicio == 'nao':
        break
    else:
        print('Opção invalida, tente novamente: ')
print('Obrigado por jogar!')