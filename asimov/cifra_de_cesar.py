alfabeto_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


frase_crua = input('Insira a frase a ser criptografada:\n-')
chave = int(input('Insira o número da sua chave:\n-')) - 1

i = 0
frase_criptografada = ''

for letra in frase_crua:
    if letra in alfabeto_lower:
        for l in alfabeto_lower:
            i += 1
            if l == letra:
                frase_criptografada += alfabeto_lower[i + chave]
                i=0
                break
    elif letra in alfabeto_upper:
        for l in alfabeto_upper:
                i += 1
                if l == letra:
                    frase_criptografada += alfabeto_upper[i + chave]
                    i=0
                    break
    else:
         frase_criptografada += letra

print(f'Sua chave criptografada é:\n {frase_criptografada}')