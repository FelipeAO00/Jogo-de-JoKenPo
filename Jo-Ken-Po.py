from random import randint

from colorama import Fore, Style, init

# Ativar o Colorama no Windows
init(autoreset=True)
'''
print(Fore.RED + "Este texto é vermelho")
print(Fore.BLUE + "Este texto é azul")
print(Fore.GREEN + "Este texto é verde")

# Pode combinar com estilos
print(Fore.RED + Style.BRIGHT + "Vermelho brilhante")
'''

'''
print(f'Papel com Papel', Fore.BLUE + 'EMPATE!')

'''



opcoes = 'Pedra' , 'Papel' , 'Tesoura'

computador = randint(0,2)

print(Fore.LIGHTWHITE_EX + Style.BRIGHT +'===== JO-KEN-PO =====')
print("""
[0] Pedra 
[1] Papel
[2] Tesoura 
""")
jogador=int(input('Selecione sua jogada: '))

print(f'O jogador jogou {(opcoes[jogador])}')
print(f'O computador Jogou {(opcoes[computador])}')


if jogador == 0: #computador jogou pedra
    if computador == 0:
        print('Pedra com Pedra,', Fore.BLUE + Style.BRIGHT + 'EMPATE!')

    elif computador == 1:
        print('Papel com Pedra,', Fore.RED + Style.BRIGHT + 'Vitoria do Computador')

    elif computador == 2:
        print('Tesoura com Pedra,', Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Vitoria do Jogador')

    else:
        print(Fore.BLACK + Style.BRIGHT + 'Algo deu errado')

elif jogador == 1:#computador jogou papel
    if computador == 0:
        print('Papel com Pedra,', Fore.RED + Style.BRIGHT + 'Vitoria do Computador')

    elif computador == 1:
        print(f'Papel com Papel,', Fore.BLUE + Style.BRIGHT + 'EMPATE!')

    elif computador == 2:
        print('Papel com Tesoura,', Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Vitoria do Jogador')

    else:
        print(Fore.BLACK + Style.BRIGHT + 'Algo deu errado')

elif jogador == 2:#computador jogou tesoura
    if computador == 0:
        print('Tesoura com Pedra,', Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Vitoria do Jogador')

    elif computador == 1:
        print('Tesoura com Papel,', Fore.RED + Style.BRIGHT + 'Vitoria do Computador')

    elif computador == 2:
        print('Tesoura com Tesoura,', Fore.BLUE + Style.BRIGHT + 'EMPATE!')

    else:
        print(Fore.BLACK + Style.BRIGHT + 'Algo deu errado')

