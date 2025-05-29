from os import system
from random import choice
from time import sleep
def titulo(t):
    print('\033[36m='*20, t, '='*20)
lista_palavras = {
                'comida' : ['arroz carreteiro', 'feijoada', 'coxinha', 'moqueca de peixe', 'acarajé', 'baião de dois', 'pão de queijo', 'pamonha', 'carne de sol'],
                'esporte' : ['futebol', 'basquete', 'críquete', 'rúgbi', 'beisebol'],
                'profissão' : ['engenharia de pesca', 'gestão ambiental', 'fonoaudiologia', 'analise e desenvolvimento de sistemas'],
                'tudo':  ['arroz carreteiro', 'feijoada', 'coxinha', 'moqueca de peixe', 'acarajé', 'baião de dois', 'pão de queijo', 'pamonha', 'carne de sol',
                          'futebol', 'basquete', 'críquete', 'rúgbi', 'beisebol','engenharia de pesca', 
                          'gestão ambiental', 'fonoaudiologia', 'analise e desenvolvimento de sistemas']}
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
    inicio = str(input('\033[1;30mDeseja jogar [s/n]: \033[m')).lower()
    system('cls')
    if inicio == 'sim' or inicio == 's':
        while True:
            letra_usuario = []
            letra_do_jogador_esp = ''
            system('cls')
            titulo('SELEÇÃO DO TEMA')
            print('\033[1;30mEscolha o tema da palavra \033[m')
            print('\033[1;30m[1]Comida\n[2]Esporte\n[3]Profissão\n[4]Aleatorio\n[5]Sair\033[m')
            opc = str(input('\033[1;30mInforme o tema: \033[m'))
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
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        else:
                            system('cls')
                            titulo('COMIDA')
                            print(jogador)
                            print('\033[1;30mLetra já digitadas: \033[m', end='')
                            for p in letra_usuario:
                                print(p ,end='\033[33m \033[m')
                            newpalavra =''
                            print('\n\033[30mSe quiser chutar a palavra interia digite "chutar"\033[m')
                            letra_do_jogador = str(input('\n\033[1;30mEscolha uma letra: \033[m')).lower()
                            if len(letra_do_jogador) == 1:
                                if letra_do_jogador not in letra_usuario:
                                    if letra_do_jogador in letras_especiais.keys():
                                        for letra in palavra:
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    letra_usuario.append(letra_do_jogador)
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
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
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                else:
                                    cont = 6
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
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
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        else:
                            system('cls')
                            titulo('ESPORTE')
                            print(jogador)
                            print('\033[1;30mLetra já digitadas: \033[m', end='')
                            for p in letra_usuario:
                                print(p ,end='\033[33m \033[m')
                            newpalavra =''
                            print('\n\033[30mSe quiser chutar a palavra interia digite "chutar"\033[m')
                            letra_do_jogador = str(input('\n\033[1;30mEscolha uma letra: \033[m')).lower()
                            if len(letra_do_jogador) == 1:
                                if letra_do_jogador not in letra_usuario:
                                    if letra_do_jogador in letras_especiais.keys():
                                        for letra in palavra:
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    letra_usuario.append(letra_do_jogador)
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
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
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                else:
                                    cont = 6
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
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
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        else:
                            system('cls')
                            titulo('PROFISSÃO')
                            print(jogador)
                            print('\033[1;30mLetra já digitadas: \033[m', end='')
                            for p in letra_usuario:
                                print(p ,end='\033[33m \033[m')
                            newpalavra =''
                            print('\n\033[30mSe quiser chutar a palavra interia digite "chutar"\033[m')
                            letra_do_jogador = str(input('\n\033[1;30mEscolha uma letra: \033[m')).lower()
                            if len(letra_do_jogador) == 1:
                                if letra_do_jogador not in letra_usuario:
                                    if letra_do_jogador in letras_especiais.keys():
                                        for letra in palavra:
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    letra_usuario.append(letra_do_jogador)
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
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
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                else:
                                    cont = 6
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
                                sleep(2)
                case '4':
                    palavra = choice(lista_palavras['total'])
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
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        else:
                            system('cls')
                            titulo('ALEATORIO')
                            print(jogador)
                            print('\033[1;30mLetra já digitadas: \033[m', end='')
                            for p in letra_usuario:
                                print(p ,end='\033[33m \033[m')
                            newpalavra =''
                            print('\n\033[30mSe quiser chutar a palavra interia digite "chutar"\033[m')
                            letra_do_jogador = str(input('\n\033[1;30mEscolha uma letra: \033[m')).lower()
                            if len(letra_do_jogador) == 1:
                                if letra_do_jogador not in letra_usuario:
                                    if letra_do_jogador in letras_especiais.keys():
                                        for letra in palavra:
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    letra_usuario.append(letra_do_jogador)
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
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
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                else:
                                    cont = 6
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
                                sleep(2)
                case '5': 
                    break
    elif inicio == 'não' or  inicio == 'n' or inicio == 'nao':
        break
    else:
        print('Opção invalida, tente novamente: ')
print('Obrigado por jogar!')