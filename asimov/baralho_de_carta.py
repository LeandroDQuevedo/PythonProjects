import random


numeros = [str(n) for n in range(2, 11)]
figuras = ['J', 'Q', 'K', 'A']
cartas = numeros + figuras

copas = [f'{c}♥' for c in cartas]
ouros = [f'{c}♦' for c in cartas]
paus = [f'{c}♣' for c in cartas]
espadas = [f'{c}♠' for c in cartas]

def gerar_baralho (quantidade_baralhos, coringas):
    baralho = quantidade_baralhos * (copas + ouros + paus + espadas)
    if coringas > 0:
        for i in range(coringas):
            jk = str(f'JK{i+1}')
            baralho.append(jk)
    random.shuffle(baralho)
    return baralho

def dar_as_cartas (jogadores, cartas):
    jogadores_baralho = {}
    for formacao_jogadores in range(jogadores):
        jogador_baralho = []
        
        for _ in range(cartas):
            carta_selecionada = baralho.pop(0)
            jogador_baralho.append(carta_selecionada)
        jogadores_baralho.update({f"jogador {formacao_jogadores+1}": jogador_baralho})
    
    return jogadores_baralho
        
        
#Insere os parametros do jogo
            
qntd_baralho = int(input("Digite a quantidade de baralhos.\n-"))
qntd_coringa = int(input("Digite a quantidade de coringas.\n-"))
qntd_jogadores = int(input("Digite a quantidade de jogadores.\n-"))
qntd_cartas = int(input("Digite a quantidade de cartas.\n-"))

#Gera o baralho e mostra já embaralhado

baralho = gerar_baralho(qntd_baralho,qntd_coringa)
print(f'O baralho tem {len(baralho)} cartas')
print(', '.join(baralho))


#Distribui as cartas aos jogadores

jogadores = dar_as_cartas(qntd_jogadores,qntd_cartas)
print(f'O baralho tem {len(baralho)} cartas')
print(', '.join(baralho))


#Mostra as mãos dos jogadores
for player in jogadores:
    print(f'Mão do {player}:')
    print('\n'.join(jogadores.get(player)))




    