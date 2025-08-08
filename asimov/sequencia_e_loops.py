# # Desafio 1

# num = [1,12,23,10,2,3,4]
# add = 0

# for n in num:
#     add += n
# med = add/len(num)

# print(len(num))
# print(add)
# print(med)

# # Desafio 2

# num = [1,12,23,10,2,3,4]
# big = 0
# for n in num:
#     if n > big:
#         big = n
# print(big)

# # Desafio 3

# words = ['pala', 'limpo', 'esponja', 'beterraba', 'almondega']

# for word in words:
#     if len(word) >= 5:
#         print(word)

#Desafio 4

num1_list = [1,12,5,10,9,3,4]
num2_list = [4,12,23,10,2,3,1]
and_num = []

for i in range(len(num1_list)):
    n1 = num1_list[i]
    for n2 in num2_list:
        if n1 == n2:
            and_num.append(n1)
and_num.sort()
print(f'Os número da primeira lista são: {num1_list}')
print(f'Os número da segunda lista são: {num2_list}')
print(f'Os números que se repetem são: {and_num}')


