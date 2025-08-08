# Controle de Fluxo
import random
# Desafio 1

# user = 'leandro'
# psw = '1234@'

# user_log = input('Usuário:')
# psw_log = input('Senha:')

# if user == user_log and psw == psw_log:
#     print('Login executado com sucesso!')
# elif user == user_log and psw != psw_log:
#     print('Senha incorreta!')
# else:
#     print('Usuário incorreto!')

# input()

# Desafio 2

num = 1,2,3,4,5,6,7,8,9,10
pick_num = random.choice(num)

print(pick_num)
for i in range(3):
    answ = int(input('Qual o num?'))
    if answ == pick_num:
        print(f'\nAcertou na {i+1} tentativa!')
        break
    elif answ > pick_num:
        print('Menor')
    else:
        print('Maior')

print('\n______FIM______')

input()