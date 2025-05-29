#Importando as bibliotecas
from os import system
from random import choice
from time import sleep
#Criando uma função para exibir titulo
def titulo(t):
    print('\033[36m='*20, t, '='*20)
#Lista das palavras que serão usadas
lista_palavras = {
                'comida' : ['arroz carreteiro', 'feijoada', 'coxinha', 'moqueca de peixe', 'acarajé', 'baião de dois', 'pão de queijo', 'pamonha', 'carne de sol'],
                'esporte' : ['futebol', 'basquete', 'críquete', 'rúgbi', 'beisebol'],
                'profissão' : ['engenharia de pesca', 'gestão ambiental', 'fonoaudiologia', 'analise e desenvolvimento de sistemas'],
                'tudo':  ['arroz carreteiro', 'feijoada', 'coxinha', 'moqueca de peixe', 'acarajé', 'baião de dois', 'pão de queijo', 'pamonha', 'carne de sol',
                          'futebol', 'basquete', 'críquete', 'rúgbi', 'beisebol','engenharia de pesca', 
                          'gestão ambiental', 'fonoaudiologia', 'analise e desenvolvimento de sistemas']}
#Lista para cuidar de caracter acentuado
letras_especiais = {'u' :['ú', 'ù', 'û'],
                    'i' : ['í', 'ì', 'î'],
                    'o' : ['ò', 'ó', 'õ', 'ô'],
                    'e' : ['é', 'è', 'ê'],
                    'c' : ['ç'],
                    'a' : ['á', 'à', 'â', 'ã']}
#Contador de derrotas e vitorias
conta_vitorias = 0
conta_derrotas = 0
#Iniciando código
while True:
    system('cls')
    titulo('INICIO')
    #Perguntando se o usuario quer jogar
    inicio = str(input('\033[1;30mDeseja jogar [s/n]: \033[m')).lower()
    system('cls')
    #Verificando se a opção foi para iniciar
    if inicio == 'sim' or inicio == 's':
        #Iniciando o jogo
        while True:
            #Iniciando a lista para armazenar as letras digitadas
            letra_usuario = []
            #Variavel para armazenar caracter especial
            letra_do_jogador_esp = ''
            system('cls')
            #Selecionando o tema que quer jogar
            titulo('SELEÇÃO DO TEMA')
            print('\033[1;30mEscolha o tema da palavra \033[m')
            print('\033[1;30m[1]Comida\n[2]Esporte\n[3]Profissão\n[4]Aleatorio\n[5]Sair\033[m')
            opc = str(input('\033[1;30mInforme o tema: \033[m'))
            #Verificando a opção escolhida
            match opc:
                case '1':
                    #Selecionando aleatoriamente uma palavra
                    palavra = choice(lista_palavras['comida'])
                    #Contador de erros
                    cont = 0
                    #Variavel para armazenar as letras certar
                    jogador = ''
                    #Criando a estrutura da forca
                    for letra in palavra:
                        #Verificando se a espaço  e adicionando ele
                        if letra == ' ':
                            jogador +=' '
                        #Adicionando um - para cada caracter
                        else:
                            jogador += '-'
                    #Começando a forca
                    while True:
                        #Verificando se o jogador acertou a palavra
                        if jogador == palavra:
                            system('cls')
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Verificando se o jogador perdeu
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Lobby do jogo
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
                            #Verificando se respeito o limite de um caracter
                            if len(letra_do_jogador) == 1:
                                #Verificando se a letra não foi digitada
                                if letra_do_jogador not in letra_usuario:
                                    #Verificando se a letra pode ser um caracter especial
                                    if letra_do_jogador in letras_especiais.keys():
                                        #Analisando se a letra estra em caracter especial
                                        for letra in palavra:
                                            #Acicionando o caracter especial a lista de já digitados
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    #Adicionando a letra do jogador em letras já digitadas
                                    letra_usuario.append(letra_do_jogador)
                                    #Verificando se a letra está na palavra
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
                                        #Imprimindo novo layaut do jogo
                                        for letra in palavra:
                                            if letra in letra_usuario:
                                                newpalavra += letra
                                            elif letra == ' ':
                                                newpalavra +=' '
                                            else:
                                                newpalavra += '-'  
                                        jogador = newpalavra
                                    #Verificando se aletra não pertence a palavra                                        
                                    else:
                                        system('cls')
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                #Verificando se a letra já foi digitada
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            #Verificando se o jogador quer chutar a palavra
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                #Verificando se o chute foi correto
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                #Verificando se o jogador não quer chutar
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                #Verificando se o jogador errou o chute
                                else:
                                    cont = 6
                            #Verificando se o jogador digitou uma opção invalida
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
                                sleep(2)
                case '2':
                    #Selecionando aleatoriamente uma palavra
                    palavra = choice(lista_palavras['esporte'])
                    #Contador de erros
                    cont = 0
                    #Variavel para armazenar as letras certar
                    jogador = ''
                    #Criando a estrutura da forca
                    for letra in palavra:
                        #Verificando se a espaço  e adicionando ele
                        if letra == ' ':
                            jogador +=' '
                        #Adicionando um - para cada caracter
                        else:
                            jogador += '-'
                    #Começando a forca
                    while True:
                        #Verificando se o jogador acertou a palavra
                        if jogador == palavra:
                            system('cls')
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Verificando se o jogador perdeu
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Lobby do jogo
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
                            #Verificando se respeito o limite de um caracter
                            if len(letra_do_jogador) == 1:
                                #Verificando se a letra não foi digitada
                                if letra_do_jogador not in letra_usuario:
                                    #Verificando se a letra pode ser um caracter especial
                                    if letra_do_jogador in letras_especiais.keys():
                                        #Analisando se a letra estra em caracter especial
                                        for letra in palavra:
                                            #Acicionando o caracter especial a lista de já digitados
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    #Adicionando a letra do jogador em letras já digitadas
                                    letra_usuario.append(letra_do_jogador)
                                    #Verificando se a letra está na palavra
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
                                        #Imprimindo novo layaut do jogo
                                        for letra in palavra:
                                            if letra in letra_usuario:
                                                newpalavra += letra
                                            elif letra == ' ':
                                                newpalavra +=' '
                                            else:
                                                newpalavra += '-'  
                                        jogador = newpalavra
                                    #Verificando se aletra não pertence a palavra                                        
                                    else:
                                        system('cls')
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                #Verificando se a letra já foi digitada
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            #Verificando se o jogador quer chutar a palavra
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                #Verificando se o chute foi correto
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                #Verificando se o jogador não quer chutar
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                #Verificando se o jogador errou o chute
                                else:
                                    cont = 6
                            #Verificando se o jogador digitou uma opção invalida
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
                                sleep(2)
                case '3':
                    #Selecionando aleatoriamente uma palavra
                    palavra = choice(lista_palavras['PROFISSÃO'])
                    #Contador de erros
                    cont = 0
                    #Variavel para armazenar as letras certar
                    jogador = ''
                    #Criando a estrutura da forca
                    for letra in palavra:
                        #Verificando se a espaço  e adicionando ele
                        if letra == ' ':
                            jogador +=' '
                        #Adicionando um - para cada caracter
                        else:
                            jogador += '-'
                    #Começando a forca
                    while True:
                        #Verificando se o jogador acertou a palavra
                        if jogador == palavra:
                            system('cls')
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Verificando se o jogador perdeu
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Lobby do jogo
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
                            #Verificando se respeito o limite de um caracter
                            if len(letra_do_jogador) == 1:
                                #Verificando se a letra não foi digitada
                                if letra_do_jogador not in letra_usuario:
                                    #Verificando se a letra pode ser um caracter especial
                                    if letra_do_jogador in letras_especiais.keys():
                                        #Analisando se a letra estra em caracter especial
                                        for letra in palavra:
                                            #Acicionando o caracter especial a lista de já digitados
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    #Adicionando a letra do jogador em letras já digitadas
                                    letra_usuario.append(letra_do_jogador)
                                    #Verificando se a letra está na palavra
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
                                        #Imprimindo novo layaut do jogo
                                        for letra in palavra:
                                            if letra in letra_usuario:
                                                newpalavra += letra
                                            elif letra == ' ':
                                                newpalavra +=' '
                                            else:
                                                newpalavra += '-'  
                                        jogador = newpalavra
                                    #Verificando se aletra não pertence a palavra                                        
                                    else:
                                        system('cls')
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                #Verificando se a letra já foi digitada
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            #Verificando se o jogador quer chutar a palavra
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                #Verificando se o chute foi correto
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                #Verificando se o jogador não quer chutar
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                #Verificando se o jogador errou o chute
                                else:
                                    cont = 6
                            #Verificando se o jogador digitou uma opção invalida
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
                                sleep(2)
                case '4':
                   #Selecionando aleatoriamente uma palavra
                    palavra = choice(lista_palavras['tudo'])
                    #Contador de erros
                    cont = 0
                    #Variavel para armazenar as letras certar
                    jogador = ''
                    #Criando a estrutura da forca
                    for letra in palavra:
                        #Verificando se a espaço  e adicionando ele
                        if letra == ' ':
                            jogador +=' '
                        #Adicionando um - para cada caracter
                        else:
                            jogador += '-'
                    #Começando a forca
                    while True:
                        #Verificando se o jogador acertou a palavra
                        if jogador == palavra:
                            system('cls')
                            print('\033[32mVocê ganhou!\033[m')
                            conta_vitorias += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Verificando se o jogador perdeu
                        elif cont == 6:
                            system('cls')
                            print('\033[33mVocê perdeu!\033[m')
                            conta_derrotas += 1
                            print(f'\033[1;30mVocê jogou {conta_derrotas + conta_vitorias} \nVitorias: {conta_vitorias} \nDerrotas: {conta_derrotas}\033[m')
                            sleep(2)
                            break
                        #Lobby do jogo
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
                            #Verificando se respeito o limite de um caracter
                            if len(letra_do_jogador) == 1:
                                #Verificando se a letra não foi digitada
                                if letra_do_jogador not in letra_usuario:
                                    #Verificando se a letra pode ser um caracter especial
                                    if letra_do_jogador in letras_especiais.keys():
                                        #Analisando se a letra estra em caracter especial
                                        for letra in palavra:
                                            #Acicionando o caracter especial a lista de já digitados
                                            if letra in letras_especiais[letra_do_jogador]:
                                                pos = letras_especiais[letra_do_jogador].index(letra)
                                                letra_usuario.append(letras_especiais[letra_do_jogador][pos])
                                                letra_do_jogador_esp = letras_especiais[letra_do_jogador][pos]
                                    #Adicionando a letra do jogador em letras já digitadas
                                    letra_usuario.append(letra_do_jogador)
                                    #Verificando se a letra está na palavra
                                    if(letra_do_jogador in palavra) or (letra_do_jogador_esp in palavra):
                                        #Imprimindo novo layaut do jogo
                                        for letra in palavra:
                                            if letra in letra_usuario:
                                                newpalavra += letra
                                            elif letra == ' ':
                                                newpalavra +=' '
                                            else:
                                                newpalavra += '-'  
                                        jogador = newpalavra
                                    #Verificando se aletra não pertence a palavra                                        
                                    else:
                                        system('cls')
                                        print(f'\033[33mLetra não pertence a palavra! \nVocê ainda tem {5-cont} chances\033[m')
                                        sleep(2)
                                        cont += 1
                                    system('cls')
                                #Verificando se a letra já foi digitada
                                else:
                                    print('\033[33mA letra já foi digitada antes, tente novamente!\033[m')
                                    sleep(2)
                            #Verificando se o jogador quer chutar a palavra
                            elif letra_do_jogador == 'chutar':
                                system('cls')
                                titulo('ALL-WIN')
                                print(jogador)
                                print('\033[30mAo digitar uma palavra você estará arriscando tudo, \nse quiser cancelar digite "cancelar!"\n\033[m')
                                letra_do_jogador = str(input('\033[30mInforme a palavra completa: \033[m'))
                                #Verificando se o chute foi correto
                                if letra_do_jogador == palavra:
                                    jogador = palavra
                                #Verificando se o jogador não quer chutar
                                elif letra_do_jogador == 'cancelar':
                                    cont = cont
                                #Verificando se o jogador errou o chute
                                else:
                                    cont = 6
                            #Verificando se o jogador digitou uma opção invalida
                            else:
                                system('cls')
                                print('\033[33mDigite apenas uma letra!\033[m')
                                sleep(2)
                case '5': 
                    #Finalizando o jogo
                    break
    #Verificando se o usuario não quer mais jogar
    elif inicio == 'não' or  inicio == 'n' or inicio == 'nao':
        #Finalizando o programa
        break
    #Verificando se o usuario digitou uma opção valida
    else:
        print('Opção invalida, tente novamente: ')
print('Obrigado por jogar!')