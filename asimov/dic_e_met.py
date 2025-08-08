# texto = """

# Python é uma linguagem de programação de alto nível,[10] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991

# A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional

# Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a objetos, imperativo, funcional e procedural.

# O nome Python teve a sua origem no grupo humorístico britânico Monty Python,[13] criador do programa Monty Python's Flying Circus, embora muitas pessoas façam associação com o réptil do mesmo nome (em português, píton ou pitão)

# """
# texto = texto.lower()
# vogais = ['a', 'e', 'i', 'o', 'u']
# totais_vogais = 0

# for letra in vogais:
#     print(f'Seu texto tem {texto.lower().count(letra)} letras {letra.upper()}')
#     totais_vogais += texto.lower().count(letra)

# print(f'O total de vogais é: {totais_vogais}')

# Desafio 2

Capitais = {
    'Brasil':'Brasília',
    'França':'Paris',
    'Estados Unidos':'Washington',
    'Argentina':'Buenos Aires',
    'Canadá':'Ottawa'
    }
quantidade_respostas = 0
acertos = 0

print('- '*7 + 'Bem vindo ao jogo das Capitais' + ' -'*7)
s = ''
while s != 's':
    s = input('Deseja iniciar? (s para iniciar)')

if s == 's':
    for pais in Capitais:
        chute = input(f'Qual a capital do país {pais}?\n')
        quantidade_respostas += 1
        if chute == Capitais[pais]:
            acertos += 1
        cont = input('Deseja continuar? (s para continuar)')
        if cont != s:
            break
        else:
            continue

print('- '*7 + 'FIM DO JOGO' + '- '*7)
print(f'\nVocê teve {acertos} acertos')
print(f'Com uma precisão de {quantidade_respostas/acertos*100}%')
            
        
